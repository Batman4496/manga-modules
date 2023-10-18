import React from 'react';

type MangaProps = {
  params: {}
};

function Manga(props: MangaProps) {
  const { params } = props;
  return (
    <div>{JSON.stringify(params)}</div>
  );
}

export default Manga;