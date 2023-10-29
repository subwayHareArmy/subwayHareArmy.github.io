import { rehypeHeadingIds } from "@astrojs/markdown-remark";
import mdx from "@astrojs/mdx";
import react from "@astrojs/react";
import sitemap from "@astrojs/sitemap";
import { defineConfig } from "astro/config";
import rehypeAutolinkHeadings from "rehype-autolink-headings";

import { autolinkConfig } from "./plugins/rehype-autolink-config";

export default defineConfig({
  site: "https://subwayharearmy.github.io",
  integrations: [react(), mdx(), sitemap()],
  markdown: {
    rehypePlugins: [rehypeHeadingIds, [rehypeAutolinkHeadings, autolinkConfig]],
  },
  vite: {
    optimizeDeps: {
      exclude: ["fsevents"],
    },
  },
});
