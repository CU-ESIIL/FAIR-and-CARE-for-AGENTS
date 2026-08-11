import { defineConfig, devices } from '@playwright/test';

const localBaseURL = 'http://127.0.0.1:8000/FAIR-and-CARE-for-AGENTS/';
const suppliedBaseURL = process.env.PLAYWRIGHT_TEST_BASE_URL;

export default defineConfig({
  testDir: './tests',
  testMatch: 'site.spec.ts',
  fullyParallel: true,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: process.env.CI
    ? [['github'], ['html', { open: 'never' }]]
    : [['list']],
  use: {
    baseURL: suppliedBaseURL ?? localBaseURL,
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
  },
  webServer: suppliedBaseURL
    ? undefined
    : {
        command: 'python3 -m mkdocs serve --dev-addr=127.0.0.1:8000',
        url: localBaseURL,
        reuseExistingServer: !process.env.CI,
        timeout: 120_000,
      },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
