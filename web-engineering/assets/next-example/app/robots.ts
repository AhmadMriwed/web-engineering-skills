import type { MetadataRoute } from "next";
import { origin } from "../catalog";

export default function robots(): MetadataRoute.Robots {
  return { rules: { userAgent: "*", disallow: "/" }, sitemap: `${origin}/sitemap.xml` };
}
