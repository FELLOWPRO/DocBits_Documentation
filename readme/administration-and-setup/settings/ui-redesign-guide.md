# UI Redesign Guide

Release R1.0 23/24 ships a refreshed user interface across DocBits — a redesigned sign-in, a collapsible sidebar, reorganised settings, anchor-based navigation, and inline help. This page walks through what's different and how to use the new affordances.

## Redesigned login and authentication

The sign-in screen, password reset, and SSO entry points have been reworked to match the new design system.

<figure><img src="../../.gitbook/assets/ui-redesign-login.png" alt="Redesigned login screen"><figcaption><p>The new sign-in screen — clearer hierarchy, brand colour applied to the action button.</p></figcaption></figure>

What changed:

* A single primary action ("Sign in") is now the focus of the page.
* SSO providers (Microsoft 365, Google, Infor OS) appear as labelled buttons under the email field.
* Password reset and "Need help signing in?" links are grouped at the bottom for visual calm.
* Error messages appear directly under the input that triggered them, instead of as a banner.

The flow is unchanged — only the layout and styling were updated.

## Collapsible sidebar

The main sidebar can now be collapsed to an icon-only mini mode, freeing up horizontal space on the current screen.

* Click the toggle at the top of the sidebar to switch between expanded and mini mode.
* In mini mode, hover an icon to see its label.
* Mini mode is remembered per browser, so the next visit opens in the same state.

For deeper customisation of the sidebar itself — reorder, hide, pin items — see [Customizable Sidebar](../../end-user-and-partner-section/end-user-section/customizable-sidebar.md).

## Organised settings subcategories

Settings has been regrouped into clearer subcategories so related options sit together. Top-level groups now reflect how administrators actually work:

* **Company & Users** — company details, users, groups, permissions.
* **Document Processing** — modules, OCR, decision trees, rules.
* **Document Types** — document type definitions and per-type settings (scripts, EDI, fields, model training).
* **Integration** — API keys, exports, ERP connections.
* **Logging & Search** — access audit, analytics, fulltext index.
* **Setup** — supplier portal, watchdog.

Page positions inside each group have been adjusted to put the most frequently used pages near the top.

## Anchor-based navigation inside long pages

Settings pages with many sections (such as Global Settings or Document Type configuration) now expose anchor links in the page header. Click an anchor to jump to that section and the URL updates so the link is shareable.

The current section is highlighted in the anchor list as you scroll, making it easier to keep your place on long pages.

## Context help panels

A small help icon now appears in the header of most settings pages and feature dialogs. Clicking it opens the matching page on the [DocBits documentation site](https://docs.docbits.com/) in a new tab — no more searching the docs for the right page.

<mark>The help icon is locale-aware. If your user language is German, French, Spanish, Dutch, Italian, or Chinese, the icon opens the matching translated page on the docs site. Languages without a published translation fall back to English.</mark>

## What hasn't changed

The redesign is visual and navigational — no settings, fields, or processing behaviour have changed. Existing URLs continue to work, so bookmarked links and external integrations are not affected.
