import Image from "@/components/Image"
import getHotMangas from "@/actions/get-hot-mangas";
import MangaCard from "@/components/manga-card";

type HomeProps = {
  params: {
    source: number
  }
}

export default async function Home({ params }: HomeProps) {
  const { result, source } = await getHotMangas(params.source);
  return (
      <div className="grid grid-cols-2 md:grid-cols-4 text-center">
        {result.map(manga => (
          <MangaCard 
            key={manga.title}
            manga={manga} 
            source={params.source} 
            imageSource={source}
          />
        ))}
      </div>
  )
}
