# Personal Site [![Deployment Badge](https://github.com/kevinthedang/kevinthedang.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/kevinthedang/kevinthedang.github.io/deployments) [![Release Badge](https://img.shields.io/github/v/release/kevinthedang/Space-Guardians?logo=github)](https://github.com/kevinthedang/kevinthedang.github.io/releases/latest) 

## Running `gh-pages` Deployment
* For the automated process, please refer to `.github/workflows/deploy.yml`
* The manual way:
   * If you do not care about deployment naming, just run `npm run deploy` in the root directory of your project.
   * If you do care about deployment naming, consider writing a python script or just run `npm run deploy -- -m DEPLOY_MESSAGE`


## What do I use for development?
* [React](https://react.dev/)
* [TypeScript](https://www.typescriptlang.org/)
* [Vite](https://vitejs.dev/)
   * [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc)
   * [SWC](https://swc.rs/) for Fast Refresh (I believe only in development)
* [gh-pages](https://www.npmjs.com/package/gh-pages)

## Resources
* Where I found the [fonts](https://sabotagestudio.com/streamers/sea-of-stars/#fonts)

## Acknowledgements
* Massive inspiration from [Sharlene Yap](https://sharyap.com/)
   * Check out her other work [here](https://www.youtube.com/@shar)! She's an animator!