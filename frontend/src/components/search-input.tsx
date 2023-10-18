'use client';
import React from 'react';
import { useRouter } from 'next/navigation';

function SearchInput() {

  function search(e: React.FormEvent<HTMLFormElement>) {
    
  }

  return (
    <form onSubmit={search}>
      <input type="text" className="p-2" placeholder="Search..." />
    </form>
  );
}

export default SearchInput;