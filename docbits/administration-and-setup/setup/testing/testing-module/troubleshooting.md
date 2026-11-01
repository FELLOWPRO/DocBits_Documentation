# Troubleshooting

## I cannot find Testing in Settings

The page is only shown to organisation admins. Ask an organisation admin of your organisation.

## The page says Testing is switched off

An organisation admin must switch on **Enable Testing for the organization** at the top of the page.
Until then, nothing runs, also not from an AI assistant or from outside.

## My run failed

Open the log in the **Logs** tab and look at the first failed step and its error code:

| You see | Usually means | What to do |
|---|---|---|
| An element was not found or not visible | The page looks different in your organisation, or loads slowly | Open the page yourself and check it; adjust your own template, or check the input values |
| A field or status does not match | The document has another value than the input expects | Check the document; correct the expected value in the input |
| The page could not be opened | Wrong document ID, or no permission | Check the ID in the input and the permissions of the user who started the tab |
| Timed out | The step or the whole test took too long | Run again; if it repeats, check the page performance |
| Blocked by the environment | The test writes data on a customer environment | Confirm the start, or run it on a test environment |

## My run is "Blocked"

The run could not be judged: some steps were skipped (for example a screenshot step, which the browser cannot take)
or a confirmation is missing. A blocked run is never counted as passed. Remove the step from your own template, or
start it again with the confirmation.

## "Register a browser session to start" / no tab accepts starts

Starts from an AI assistant or from outside need a browser tab with **Allow starts from outside** switched on. Open
the Inputs tab in a tab that stays open, switch it on and use its session ID. A reload ends the registration.

## The run stopped or shows Cancelled / Undeliverable

The tab that ran the test was reloaded, closed or lost its connection, or no tab answered in time. Keep the tab open
and in the foreground until the run ends, then start again.

## "Playwright templates cannot be started here yet"

Templates whose **Executor** is **Playwright** are run by your test automation. You can save inputs for them, but you
cannot start them from this page.

## I cannot delete a template

Only your organisation's own templates (**custom**) can be deleted. Built-in and default templates cannot; use
**Edit a copy** to get your own version.
