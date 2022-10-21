import React, { SVGProps } from 'react';
import { styled } from '@mui/system';
import classNames from 'classnames';

interface IProps extends SVGProps<any> {
  icon: string;
  className?: string;
  fill?: string;
  width?: string;
  height?: string;
}

const Icon = (props: IProps) => {
  const { icon, width, height, fill, className, ...others } = props;

  const StyledSVG = styled('svg')(
    () => `
    width: ${width ? width : '25px'};
    height: ${height ? height : '25px'};
    use {
      width: ${height ? height : '25px'};
      height: ${height ? height : '25px'};
    };
    fill: #fff
  `
  );
  return (
    <StyledSVG className={classNames(`iconfont`, className)} aria-hidden="true" {...others}>
      <use xlinkHref={icon} href={icon} />
    </StyledSVG>
  );
};

export default Icon;
