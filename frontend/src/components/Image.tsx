'use client';
import React, { useEffect, useState } from 'react';
import NextImage from 'next/image';
import { API_URL, IMAGES } from '@/constants/routes';

type ImageProps = {
  src: string,
  source?: string,
  alt?: string,
  fill?: boolean,
};

function Image(props: ImageProps) {
  const  {
    src, 
    source,
    alt,
    fill
  } = props;
  
  const [url, setUrl] = useState<string>(IMAGES.LOADING);
  const p = fill ? { fill: true } : { height: 300, width: 200 }

  useEffect(() => {
    if (!source) {
      return setUrl(src);
    } 

    fetch(`${API_URL}/get-image?url=${src}&referer=${source}`)
      .then(res => res.text())
      .then(res => setUrl(res));

  }, [src, source]);

  return (
    <NextImage
      src={url}
      alt={alt ?? ''}
      { ...p }
    />
  );
}

export default Image;