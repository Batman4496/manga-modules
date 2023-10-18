'use client';
import getSources from "@/actions/get-sources";
import { API_URL } from "@/constants/routes";
import React, { createContext, useContext, useEffect, useState } from "react";

export type Source = {
  id: string,
  name: string,
  url: string
}

type SourceState = { source: Source, sources: Source[] };

const SourceContext = createContext<[
  SourceState|null, React.Dispatch<React.SetStateAction<any>>
]|[]>([]);

export function useSource() {
  return useContext(SourceContext);
}

export function SourceProvider(props: React.PropsWithChildren) {
  const [source, setSource] = useState<SourceState|null>(null);

  useEffect(() => {
    getSources().then((sources: Source[]) => {
      setSource({ 
        sources: sources,
        source: sources[0]
      })
    });
  }, []);

  return (
    <SourceContext.Provider value={[source, setSource]}>
      {props.children}
    </SourceContext.Provider>
  )
}