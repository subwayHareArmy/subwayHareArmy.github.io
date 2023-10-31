import { expect, test } from "@playwright/test";

test.beforeEach(async ({ page }) => {
  await page.goto("/");
});

// TODO: Write test that will go to every page in the sitemap, and check to make sure that every page has the GA tag in it.