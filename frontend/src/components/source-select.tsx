'use client';
import React from 'react';
import { useParams, useRouter } from 'next/navigation';

export type Source = {
  id: string,
  name: string,
  url: string
}

function SourceSelect(props: { sources: Source[] }) {
  const { sources } = props;
  const router = useRouter();
  const params = useParams() as { source: string };

  function changeSource(e: React.ChangeEvent<HTMLSelectElement>) {
    const { value } = e.target;
    console.log(value);
    router.push(`/${value}`);
  }

  return (
    <select onChange={changeSource}>
      {sources.map((source) => (
        <option 
          selected={source.id == params.source} 
          key={source.id} 
          value={source.id}
        >
          {source.name}
        </option>
      ))}
    </select>
  );
}

export default SourceSelect;