import getSources from '@/actions/get-sources';
import SourceSelect from '@/components/source-select';
import ThemeSelect from '@/components/theme-select';
import React from 'react';

type MainLayoutProps = {
  children: React.ReactNode
};

async function MainLayout(props: MainLayoutProps) {
  const sources = await getSources();
  const {
    children
  } = props;
  
  return (
    <>
      <nav className="flex flex-row p-2 items-center justify-between">
        <h1 className="text-md md:text-2xl">Library</h1>
        <div className="flex flex-row gap-2">
          <SourceSelect sources={sources} />
          <ThemeSelect />
        </div>
      </nav>

      <main className="flex flex-col gap-2">
        {children}
      </main>
    </>
  );
}

export default MainLayout;