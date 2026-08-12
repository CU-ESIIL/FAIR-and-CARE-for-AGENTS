import { expect, test } from '@playwright/test';

const expectedLinks = {
  'Read the working manuscript':
    'https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science_v2.md',
  'Explore the repository':
    'https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS',
  'Visit ESIIL': 'https://esiil.org/',
  'Visit the University of Colorado Boulder': 'https://www.colorado.edu/',
  'Visit CIRES': 'https://cires.colorado.edu/',
  'Visit the U.S. National Science Foundation': 'https://www.nsf.gov/',
};

test('homepage renders its core content and assets without browser errors', async ({ page, baseURL }) => {
  const browserErrors: string[] = [];
  const failedResponses: string[] = [];
  const externalResources: string[] = [];
  const siteOrigin = new URL(baseURL!).origin;
  page.on('console', (message) => {
    if (message.type() === 'error') browserErrors.push(message.text());
  });
  page.on('pageerror', (error) => browserErrors.push(error.message));
  page.on('response', (response) => {
    if (response.status() >= 400) {
      failedResponses.push(`${response.status()} ${response.url()}`);
    }
  });
  page.on('request', (request) => {
    if (new URL(request.url()).origin !== siteOrigin) {
      externalResources.push(`${request.resourceType()} ${request.url()}`);
    }
  });

  const response = await page.goto('./');

  expect(response?.ok()).toBeTruthy();
  await expect(page).toHaveTitle(/Designing FAIR and CARE into Agentic Science/);
  await expect(page.getByRole('heading', { level: 1 })).toHaveText(
    'FAIR + CARE for Agentic Science',
  );
  await expect(
    page.getByText(
      'FAIR and CARE help people do better science. CARE-informed questions make governance harder to bypass, and agents need those practices designed into their workflows.',
    ),
  ).toBeVisible();

  const brokenImages = await page.locator('img').evaluateAll((images) =>
    images
      .filter((image) => !(image as HTMLImageElement).complete || (image as HTMLImageElement).naturalWidth === 0)
      .map((image) => image.getAttribute('alt')),
  );
  expect(brokenImages).toEqual([]);
  expect(externalResources).toEqual([]);
  expect(failedResponses).toEqual([]);
  expect(browserErrors).toEqual([]);
});

test('calls to action and institutional logo links have the intended destinations', async ({ page }) => {
  await page.goto('./');

  for (const [name, href] of Object.entries(expectedLinks)) {
    const link = page.getByRole('link', { name, exact: true });
    await expect(link).toHaveCount(1);
    await expect(link).toHaveAttribute('href', href);
  }

  const oasisLinks = page.locator('a[aria-label="Visit the OASIS home page"]');
  await expect(oasisLinks).toHaveCount(2);
  expect(await oasisLinks.evaluateAll((links) => links.map((link) => (link as HTMLAnchorElement).href))).toEqual([
    'https://cu-esiil.github.io/home/',
    'https://cu-esiil.github.io/home/',
  ]);
});

test('every local page and link resolves successfully', async ({ page, request, baseURL }) => {
  const siteRoot = new URL(baseURL!);
  const pending = [siteRoot.href];
  const visited = new Set<string>();

  while (pending.length > 0) {
    const url = pending.shift()!;
    if (visited.has(url)) continue;
    visited.add(url);

    const response = await request.get(url);
    expect(response.ok(), `${url} returned ${response.status()}`).toBeTruthy();

    await page.goto(url);
    const hrefs = await page.locator('a[href]').evaluateAll((links) =>
      links.map((link) => (link as HTMLAnchorElement).href),
    );

    for (const href of hrefs) {
      const target = new URL(href);
      target.hash = '';
      if (
        target.origin === siteRoot.origin &&
        target.pathname.startsWith(siteRoot.pathname) &&
        !visited.has(target.href)
      ) {
        pending.push(target.href);
      }
    }
  }

  expect(visited.size).toBeGreaterThan(1);
});

test('mobile layout has no horizontal overflow and keeps primary actions visible', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('./');

  await expect(page.getByRole('link', { name: 'Read the working manuscript', exact: true })).toBeVisible();
  const dimensions = await page.evaluate(() => ({
    clientWidth: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
  }));
  expect(dimensions.scrollWidth).toBeLessThanOrEqual(dimensions.clientWidth);
});

test('back-to-top control returns the reader to the beginning of the page', async ({ page }) => {
  await page.goto('./');
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
  await page.evaluate(() => window.scrollBy(0, -500));

  const backToTop = page.getByRole('button', { name: 'Back to top', exact: true });
  await expect(backToTop).toBeVisible();
  await backToTop.click();
  await expect.poll(() => page.evaluate(() => window.scrollY)).toBeLessThan(5);
});
