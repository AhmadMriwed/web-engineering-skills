import type { MetadataRoute } from "next";
import { locales, origin } from "../catalog";

export default function sitemap(): MetadataRoute.Sitemap {
  return locales.map(locale => ({ url: `${origin}/${locale}/items/atlas` }));
}
