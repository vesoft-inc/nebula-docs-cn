import { Dialog } from '@mui/material'
import * as React from 'react';
import Icon from '../Icon';
import Search from '../Search';
import styles from './index.module.less';

const { useState } = React;

const SearchDialog = () => {
  const [searchVisible, setSearchVisible] = useState(false);
  return (
    <>
      <div
        className={styles.searchIcon}
        onClick={() => {
          setSearchVisible(true);
        }}
      >
        <Icon icon="#icon-algolia-search" className={styles.search} />
      </div>
      <Dialog
        classes={{ container: styles.searchDialog }}
        onClose={() => {
          setSearchVisible(false);
        }}
        open={searchVisible}
        maxWidth={false}
      >
        <Search
          algoliaAppID='KJ8BSDU4EX'   
          algoliaSecret='e9a73b79886a3a46aa953a7bc40dbe9f'
          indexName={location.host.includes('.io') ? 'site-en' : 'site-cn'}
          onClose={() => {
            setSearchVisible(false);
          }}
        />
      </Dialog>
    </>
  );
}

export default SearchDialog