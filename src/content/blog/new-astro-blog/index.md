---
title: Moving the blog to Astro
description: for blazing fast SSG that delivers minimal JS
datePublished: 2023-10-04 22:16:00+05:30
dateModified: 2023-10-04 22:16:00+05:30
img: ["./pelicanToAstro.png"]
imgAlt: A photo describing the blog moving from using the Python Pelican library to using Astro, the JS metaframework.
# ogImage: ./daancorona_progress.png
# TODO: Find and add a hero image here
tags: ["blog", "astro"] 
visibility: public
---

WIP article.
<!-- TODO: WIP article. -->

Pelican is a great open source Static Site Generator (SSG) for Python. It provides support for themes and templates with many people offering theirs for use by others. The ability to write content in Markdown and have fast rebuild times while writing the content out to the pages was what drew me in. The plugin ecosystem was a major draw as well. However, people have moved away from it in favour of modern frameworks with more extensibility and active users.

One such framework is Astro. I can use Astro as an SSG, using the popular JS frameworks like React, Vue, Svelte, even multiple ones at the same time. 

Astro ships the smallest amount of JS, it introduces the idea of partial hydration through the use of interactive islands in a sea of non-interactivity. With directives you can choose when to ship JS to each component.

Some decisions:
- Using React, or Vue
- Typescript instead of vanilla JS
- Using in SSG mode
- Deploying to GH Pages using GH Actions
- Using Playwright for writing cross-browser testing
- pnpm as the package manager
- Google Analytics for basic analytics
- partytown for lazy-loading any scripts
- Content written in markdown 
- Astro transitions makes transition animations easy
- Sass for CSS
