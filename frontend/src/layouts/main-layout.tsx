import React from 'react';

type MainLayoutProps = {
  children: React.ReactNode
};

function MainLayout(props: MainLayoutProps) {
  const {
    children
  } = props;

  return (
    <div>MainLayout</div>
  );
}

export default MainLayout;