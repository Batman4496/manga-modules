export type Manga = {
  id?: string,
  title: string,
  url: string,
  image: string
};

export interface ApiResponse {
  result: any,
  source: string
}