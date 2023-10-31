import { rehypeHeadingIds } from "@astrojs/markdown-remark";
import mdx from "@astrojs/mdx";
import react from "@astrojs/react";
import sitemap from "@astrojs/sitemap";
import { defineConfig } from "astro/config";
import rehypeAutolinkHeadings from "rehype-autolink-headings";
import { autolinkConfig } from "./plugins/rehype-autolink-config";
import partytown from "@astrojs/partytown";

// https://astro.build/config
export default defineConfig({
  site: "https://subwayharearmy.github.io",
  integrations: [react(), mdx(), sitemap(), partytown()],
  markdown: {
    rehypePlugins: [rehypeHeadingIds, [rehypeAutolinkHeadings, autolinkConfig]],
  },
  vite: {
    optimizeDeps: {
      exclude: ["fsevents"],
    },
  },
});
