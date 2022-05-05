# gha-mobile-release

The purpose of this GitHub Action is to automate the releasing of mobile apps to the Apple
App Store and the Google Play Store.

## Inputs

| NAME                         | DESCRIPTION                                                             | TYPE      | REQUIRED | DEFAULT  |
| ---------------------------- | ----------------------------------------------------------------------- | --------- | -------- | -------- |
| `expo-username`              | The username for the expo account being released from                   | `string`  | `true`   |          |
| `expo-password`              | The password for the expo account being released from                   | `string`  | `true`   |          |
| `expo-app-specific-password` | The app-specific password used to submit a build to the Apple App Store | `string`  | `true`   |          |
| `release-channel`            | The channel used for OTA update releases                                | `string`  | `false`  | `stores` |
| `commit-author-email`        | The email address of the commit author                                  | `string`  | `false`  |          |
| `commit-author-name`         | The name of the commit author                                           | `string`  | `false`  |          |
| `submodules`                 | Whether to checkout submodules                                          | `boolean` | `false`  | `true`   |
| `token`                      | The token to access private repos                                       | `string`  | `false`  |          |

## Usage

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
          expo-app-specific-password: ${{ secrets.EXPO_APP_SPECIFIC_PASSWORD }}
```
