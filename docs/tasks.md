# Training Tasks Checklist

## Exercise 00 — Onboarding + Products + SQL
- [ ] Read Shopify Admin GraphQL API docs
- [ ] Understand Product / Variant basics
- [ ] Create two products (simple + variants) - Manual
- [ ] Implement a product query
- [ ] Create SQLite tables using raw SQL
- [ ] Insert queried products into SQLite using raw SQL
- [ ] Implement SELECT queries to verify inserted data

## Exercise 1 — Create Product & Collections
- [ ] Create a custom collection
- [ ] Create a smart collection (if supported/available)
- [ ] Create two products (simple + variants) - via Graphql
- [ ] Query collections
- [ ] Save created IDs into SQLite with raw SQL

## Exercise 02 — Customers + Orders
- [ ] Create a customer
- [ ] Create a order
- [ ] Save created IDs into SQLite with raw SQL

## Exercise 03 — Update Products data
- [ ] Create 2 products:
  - [ ] 1 simple product (inventory not tracked initially)
  - [ ] 1 product with variants (variant quantity starts at 100)
- [ ] Save created IDs into SQLite using raw SQL
- [ ] Update both products:
  - [ ] Set quantity to 200 for both
  - [ ] Update tags
  - [ ] Create a new collection and add products to it
  - [ ] Update product titles

## Exercise 04 — Cleanup
- [ ] Load created entity IDs from SQLite
- [ ] Delete entities in a safe order
- [ ] Delete SQLite rows after successful cleanup
- [ ] Verify Shopify admin is clean

## Exercise 05 — Redirects
- [ ] Create URL redirects in the store
- [ ] Query redirects and verify results

## Exercise 06 — Metafields
- [ ] Create metafield definition (optional)
- [ ] Set metafields on products
- [ ] Query metafields back

## Exercise 07 — Metaobjects
- [ ] Create metaobject definition (if needed)
- [ ] Create metaobject entries
- [ ] Query metaobjects

## Exercise 08 — Gift cards
- [ ] Create gift card
- [ ] Query gift cards
- [ ] Disable or adjust gift card (if supported)

## Exercise 09 — Multi-language
- [ ] Understand Translations API objects
- [ ] Add translations for a product title and a collection title (example)

## Exercise 10 — B2B companies
- [ ] Create a company
- [ ] Add a company contact
- [ ] Query company data
