# Magic8Ball

[![Build Status](https://github.com/software-students-spring2025/3-python-package-package/actions/workflows/python-package.yml/badge.svg)](https://github.com/software-students-spring2025/3-python-package-package/actions/workflows/build.yaml/badge.svg)

A lighthearted fortune-telling package that returns fortunes in various styles.

## Features

- **tell_fortune()**: Returns a random general fortune.
- **personalized_fortune(name: str)**: Returns a fortune with the user’s name.
- **fortune_by_category(category: str)**: Returns a fortune for a given category (love, career, health).
- **daily_by_birth_month(birth_month: str)**: Returns a daily fortune that remains consistent for the same day.

## Installation

Use [pipenv](https://pipenv.pypa.io/en/latest/) to set up your virtual environment:

```bash
pipenv install --dev
