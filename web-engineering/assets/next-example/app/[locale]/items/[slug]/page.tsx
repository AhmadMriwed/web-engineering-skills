import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getItem, isLocale, locales, origin } from "../../../../catalog";
import { Details } from "./Details";

type Props = { params: Promise<{ locale: string; slug: string }> };

export function generateStaticParams() {
  return [{ slug: "atlas" }];
}

async function resolveItem(params: Props["params"]) {
  const { locale, slug } = await params;
  if (!isLocale(locale)) notFound();
  const item = getItem(slug, locale);
  if (!item) notFound();
  return { locale, slug, item };
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale, slug, item } = await resolveItem(params);
  const url = (language: string) => `${origin}/${language}/items/${slug}`;
  return {
    title: item.title,
    description: item.summary,
    alternates: {
      canonical: url(locale),
      languages: Object.fromEntries(locales.map(language => [language, url(language)])),
    },
  };
}

export default async function ItemPage({ params }: Props) {
  const { locale, slug, item } = await resolveItem(params);
  const alternate = locale === "ar" ? "en" : "ar";
  return <main>
    <h1>{item.title}</h1>
    <Link href={`/${alternate}/items/${slug}`} hrefLang={alternate} lang={alternate}>
      {alternate === "ar" ? "العربية" : "English"}
    </Link>
    <Details label={locale === "ar" ? "التفاصيل" : "Details"} summary={item.summary} />
  </main>;
}
