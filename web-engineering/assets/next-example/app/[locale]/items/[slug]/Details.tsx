"use client";

import { useId, useState } from "react";

export function Details({ label, summary }: { label: string; summary: string }) {
  const id = useId();
  const [expanded, setExpanded] = useState(false);
  return <>
    <button aria-expanded={expanded} aria-controls={id} onClick={() => setExpanded(value => !value)}>
      {label}
    </button>
    <p id={id} hidden={!expanded}>{summary}</p>
  </>;
}
