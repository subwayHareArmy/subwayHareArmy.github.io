import { expect, test } from "@playwright/test";

test.beforeEach(async ({ page }) => {
  await page.goto("/");
});

test("includes correct social links", async ({ page }) => {
  const githubLink = page.getByRole("link", { name: "Github" });
  const twitterLink = page.getByRole("link", { name: "Twitter" });

  await expect(githubLink).toHaveAttribute(
    "href",
    "https://github.com/subwayharearmy"
  );
  await expect(twitterLink).toHaveAttribute(
    "href",
    "https://twitter.com/ayushyembarwar"
  );
});

test("opens social links in new tab", async ({ page }) => {
  const githubLink = page.getByRole("link", { name: "Github" });
  const twitterLink = page.getByRole("link", { name: "Twitter" });

  await expect(githubLink).toHaveAttribute("target", "_blank");
  await expect(twitterLink).toHaveAttribute("target", "_blank");
});
