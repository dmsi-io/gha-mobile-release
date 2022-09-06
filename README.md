# gha-mobile-release

The purpose of this GitHub Action is to automate the releasing of mobile apps to the Apple
App Store and the Google Play Store.

## Inputs

| NAME                         | DESCRIPTION                                                                                   | TYPE      | REQUIRED | DEFAULT      |
|:-----------------------------|:----------------------------------------------------------------------------------------------|:----------|:---------|:-------------|
| `branch`                     | The Expo branch used for OTA update releases                                                  | `string`  | `false`  | `production` |
| `commit-author-email`        | The email address of the commit author                                                        | `string`  | `false`  |              |
| `commit-author-name`         | The name of the commit author                                                                 | `string`  | `false`  |              |
| `expo-token`                 | The token for the expo account being released from                                            | `string`  | `true`   |              |
| `expo-app-specific-password` | The app-specific password used to submit a build to the Apple App Store                       | `string`  | `true`   |              |
| `git-token`                  | The git token to access private repos                                                         | `string`  | `false`  |              |
| `increment-build-number`     | 'true' if the script should automatically increment the build number in an `app.config.[jt]s` | `string`  | `false`  | `true`       |
| `platform`                   | Which platform to build for (all &#124; android &#124; ios)                                   | `string`  | `false`  | `all`        |
| `profile`                    | What profile from `eas.json` to use                                                           | `string`  | `false`  | `preview`    |
| `release-message`            | Message to use in the EAS Update                                                              | `string`  | `false`  | `Release`    |
| `submodules`                 | Whether to checkout submodules                                                                | `boolean` | `false`  | `true`       |

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
          expo-token: ${{ secrets.EXPO_TOKEN }}
          expo-app-specific-password: ${{ secrets.EXPO_APP_SPECIFIC_PASSWORD }}
```
