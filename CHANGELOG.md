# Changelog

## [Unreleased]

### Added
- Sort the cart by DVD title or cost.
- Search DVDs by category.

## [1.0.0] - 2026-11-07

### Added
- Print cart contents, including an empty-cart message.
- Search DVDs by a case-sensitive title substring.
- Calculate percentage discounts and test the application with unittest.
- Use-case documentation and Python 3.12 CI for master and release PRs.

### Changed
- Move Cart and DigitalVideoDisc into the aims package.
- Show the added-DVD confirmation in Vietnamese.

### Fixed
- Reject DVD 21 when the cart already holds 20 DVDs (#6).
- Return the discounted total and reject percentages outside 0-100.
