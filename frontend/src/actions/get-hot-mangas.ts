import axios from "axios";
import { API_URL } from "@/constants/routes";
import { ApiResponse, Manga } from "@/types/global";

interface HotMangas extends ApiResponse {
  result: Manga[];
}

export default async function getHotMangas(source: number) {
  const { data } = await axios.get(API_URL + `/${source}/hot-mangas`);
  return data as HotMangas;
}