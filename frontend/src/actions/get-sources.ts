import { API_URL } from "@/constants/routes"
import { Source } from "@/context/source-provider"

export default async function getSources() {
  const res = await fetch(API_URL + '/sources');
  const data: { sources: Source[] } = await res.json(); 
  
  return data.sources;
}