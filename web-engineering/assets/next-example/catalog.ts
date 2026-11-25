import "server-only";

export const locales = ["en", "ar"] as const;
export type Locale = (typeof locales)[number];
export const origin = "https://library.example";

export function isLocale(value: string): value is Locale {
  return locales.some(locale => locale === value);
}

export function getItem(slug: string, locale: Locale) {
  if (slug !== "atlas") return null;
  return {
    title: locale === "ar" ? "الأطلس" : "Atlas",
    summary: locale === "ar" ? "أطلس للمكتبة" : "An atlas for the library",
  };
}
