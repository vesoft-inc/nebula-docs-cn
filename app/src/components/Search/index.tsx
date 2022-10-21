import { useEffect, useState } from 'react';
import algoliasearch from 'algoliasearch/lite';
import {
  InstantSearch,
  Highlight,
  Index,
  Snippet,
  useInstantSearch,
  useSearchBox,
  useInfiniteHits,
  useMenu,
} from 'react-instantsearch-hooks-web';
import styles from './index.module.less';
import Icon from '../Icon';
interface IProps {
  algoliaAppID: string
  algoliaSecret: string
  indexName: string
  onClose: ()=> void
}

const locales = {
  'site-cn': {
    search: '搜索',
    close: '关闭',
    loadMore: '加载更多',
  },
  'site-en': {
    search: 'Search',
    close: 'Close',
    loadMore: 'LoadMore',
  }
}

const Search = (props: IProps) => {
  const { algoliaAppID, algoliaSecret, indexName } = props
  const searchClient = algoliasearch(algoliaAppID, algoliaSecret, {});

  return (
    <InstantSearch indexName={indexName} searchClient={searchClient}>
      <div className={styles.container}>
        <SearchBox {...props} />
        <Index indexName={indexName}>
          <Items indexName={indexName} />
        </Index>
      </div>
    </InstantSearch>
  );
};

let timer = null as any;
const SearchBox = (props: any) => {
  const { status } = useInstantSearch();
  const { query, refine, clear } = useSearchBox(props);
  const [value, setValue] = useState(query);
  const [isMobile, setIsMobile] = useState(false);
  const locale = locales[props.indexName]
  const { refine: refineType } = useMenu({
    attribute: 'type',
    sortBy: ['name'],
  })
  useEffect(() => {
    refineType('doc')
  }, [])

  const onChange = (e: any) => {
    setValue(e.target.value);
    if (timer) {
      clearTimeout(timer);
    }
    timer = setTimeout(() => {
      refine(e.target.value);
    }, 200);
  };
  useEffect(() => {
    if (window.innerWidth < 768) {
      setIsMobile(true);
    }
  }, []);

  const onClose = () => {
    setValue('');
    clear();
    props.onClose();
  };
  return (
    <div className={styles.search}>
      {status === 'loading' || status === 'stalled' ? (
        <Icon className={styles.searchLoading} icon="#icon-a-filesicon" />
      ) : (
        <Icon className={styles.searchIcon} icon="#icon-algolia-search" />
      )}
      <input type="text" value={value} onChange={onChange} placeholder={locale.search} autoFocus />
      {isMobile ? (
        <Icon className={styles.close} icon="#icon-algolia-close" onClick={onClose} />
      ) : (
        <>
          <Icon
            className={styles.clear}
            icon="#icon-algolia-clear"
            onClick={() => {
              setValue('');
              clear();
            }}
          />
          <span className={styles.close} onClick={onClose}>
            {locale.close}
          </span>
        </>
      )}
    </div>
  );
};

const Items = (props: {
  indexName: string
}) => {
  const { results } = useInstantSearch();
  const { hits, showMore, isLastPage } = useInfiniteHits();
  const locale = locales[props.indexName]

  if (!results.query) return null;

  return (
    <div className={styles.hits}>
      {hits.map((hit) => {
        return (
          <a className={styles.item} key={hit.objectID} href={hit.url as string} target="__blank">
            <div className={styles.title}>
              <Highlight attribute="title" hit={hit} />
            </div>
            <div className={styles.type}>
              {/* <span>{hit.type as string}</span> */}
              <span>
                <Highlight attribute="url" hit={hit}></Highlight>
              </span>
            </div>
            <p className={styles.content}>
              <Snippet attribute="content" hit={hit} />
            </p>
          </a>
        );
      })}
      {isLastPage ? null : (
        <div className={styles.showMore} onClick={showMore}>
          {locale.loadMore}
        </div>
      )}
    </div>
  );
};

export default Search;
