const path = require('path')
const babelConfig = require('./babel.config.js');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

const lessLoaderConfig = {
  loader: 'less-loader',
  options: {
    lessOptions: {
      javascriptEnabled: true,
    },
  },
};

module.exports = {
  mode: 'production',
  entry: {
    app: [path.join(__dirname, './src/vendors/iconfont.js'), path.join(__dirname, './src/app.tsx')],
  },
  module: {
    rules: [
      {
        test: /\.(j|t)sx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: babelConfig,
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader'],
      },
      {
        test: /\.module\.less$/,
        exclude: /node_modules/,
        use: [
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              modules: {
                mode: 'local',
                exportGlobals: true,
                localIdentName: '[local]__[hash:base64:5]',
                localIdentContext: path.resolve(__dirname, '..', 'src'),
              },
            },
          },
          'postcss-loader',
          lessLoaderConfig,
        ],
      }
    ],
  },
  plugins: [
    new CleanWebpackPlugin({
      cleanOnceBeforeBuildPatterns: [path.resolve(__dirname, './dist')],
    })
  ],
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx', '.json', '.css', '.less', '.woff', '.woff2', 'ttf'],
    fallback: { "url": require.resolve("url/") },
  },
  output: {
    filename: 'nebula-docs.[fullhash].js',
    path: path.resolve(__dirname, './dist'),
  },
};