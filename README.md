# gha-mobile-release

The purpose of this GitHub Action is to automate the releasing of mobile apps to the Apple
App Store and the Google Play Store.

### Usage

```yaml
name: Release

on:
  push:
    branches:
      - main

jobs:
  release:
    name: Release
    runs-on: ubuntu-latest
    steps:
      - name: Publish
        uses: dmsi-io/gha-mobile-release@main
        with:
          expo-username: ${{ secrets.EXPO_USER }}
          expo-password: ${{ secrets.EXPO_PASSWORD }}
```

