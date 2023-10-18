'use client';
import { useEffect, useState } from "react";
import { API_URL } from "@/constants/routes";
import { Axios } from "axios";
import { useSource } from "@/context/source-provider";

function useAxios() {
  const [axios, setAxios] = useState<Axios>();
  const [source] = useSource();

  useEffect(() => {
    const axios = new Axios({
      baseURL: API_URL + '/' + source?.source.id ?? 1,
      headers: {
        Accept: 'application/json'
      }
    });

    setAxios(axios);
  }, [source]);

  return axios;
}


export default useAxios;