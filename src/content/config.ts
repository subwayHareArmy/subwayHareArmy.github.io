import { defineCollection, z } from "astro:content";

export const collections = {
  notes: defineCollection({
    type: "content",
    schema: ({ image }) =>
      z.object({
        title: z.string(),
        description: z.string(),
        datePublished: z.date(),
        dateModified: z.date().optional(),
        img: image().array().optional(),
        imgAlt: z.string().optional(),
        ogImage: image().optional(),
      }),
  }),

  pages: defineCollection({
    type: "content",
    schema: ({ image }) =>
      z.object({
        title: z.string(),
        description: z.string(),
        datePublished: z.date(),
        dateModified: z.date().optional(),
        img: image().array().optional(),
        imgAlt: z.string().optional(),
        ogImage: image().optional(),
      }),
  }),

  projects: defineCollection({
    type: "data",
    schema: ({ image }) =>
      z.object({
        title: z.string(),
        description: z.string(),
        datePublished: z.date(),
        img: image().array().optional(),
        imgAlt: z.string().optional(),
        url: z.string(),
        repo: z.string().optional(),
      }),
  }),

  blog: defineCollection({
    type: 'content',
    schema: ({ image }) =>
      z.object({
        title: z.string(),
        description: z.string(),
        // // TODO: Go through all blogposts and make sure there is some good description in all the posts
        datePublished: z.date(),
        dateModified: z.date(),
        img: image().array().optional(),
        imgAlt: z.string().optional(),
        repo: z.string().optional(),
        ogImage: image().optional(),
        tags: z.array(z.string()).optional(),
        url: z.string().optional(),
        visibility: z.enum(["private", "unlisted", "public"]),
        // // TODO: Write about this visibility strategy (similar to Youtube) in the readme or somewhere
        // TODO: Add a field for authors as well, apparently that helps with SEO
      })
  })
};
