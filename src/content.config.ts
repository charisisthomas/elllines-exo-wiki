import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const wikiCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/wiki" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.string(),
    lastUpdated: z.string(),
    lang: z.enum(['el', 'en']),
    usefulLinks: z.array(z.string()).optional(),
  }),
});

const wikiEnCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/wiki-en" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.string(),
    lastUpdated: z.string(),
    lang: z.enum(['el', 'en']),
    usefulLinks: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'wiki': wikiCollection,
  'wiki-en': wikiEnCollection,
};
