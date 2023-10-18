import { Manga } from '@/types/global';
import React from 'react';
import Image from './Image';
import Link from 'next/link';

function MangaCard(props: { manga: Manga, source: number, imageSource: string }) {
  const { 
    manga,
    source,
    imageSource
  } = props;
  return (
    <div className="flex flex-col items-center justify-center gap-2">
      <Image 
        alt={manga.title}
        src={manga.image}
        source={imageSource}
      />
      <Link href={`/${source}?url=${manga.url}`}>{manga.title}</Link>
    </div>
  );
}

export default MangaCard;