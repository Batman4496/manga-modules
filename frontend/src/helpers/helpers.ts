import { API_URL } from "@/constants/routes";
import axios from "axios";

export async function getImage(url: string, source: string) {
  const { data } = await axios.get(`${API_URL}/get-image?url=${url}&referer=${source}`);

  return data;
}