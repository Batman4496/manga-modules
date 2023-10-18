'use client';
import React, { useState } from 'react';

function ThemeSelect() {
  function changeTheme(e: React.ChangeEvent<HTMLSelectElement>) {
    const { value } = e.target;
    const html = document.querySelector('html');
    
    if (value == 'dark') {
      html?.classList.add('dark');
    } else {
      html?.classList.remove('dark');
    }
  }

  return (
      <select onChange={changeTheme}>
        <option value="dark">Dark</option>
        <option value="light">Light</option>
      </select>
  );
}

export default ThemeSelect;