# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- If you are copying/pasting your HTML code, use this link: https://validator.w3.org/#validate_by_input
- (*recommended*) If you are using the live deployed site pages, use this link: https://validator.w3.org/#validate_by_uri

It's recommended to validate the live pages (each of them) using the deployed URL.
This will give you a custom URL as well, which you can use on your testing documentation.
It makes it easier to return back to a page to validate it again in the future.
The URL will look something like this:

- https://validator.w3.org/nu/?doc=https%3A%2F%2Fd3lyth.github.io%2Flunar_glow%2Findex.html

Sample HTML code validation documentation (tables are extremely helpful!):

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fd3lyth.github.io%2Flunar_glow%2Findex.html) | ![screenshot](documentation/html-validation-home.png) | Section lacks header h2-h6 warning |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fd3lyth.github.io%2Flunar_glow%2Fcontact.html) | ![screenshot](documentation/html-validation-contact.png) | obsolete iframe warnings |
| Quiz | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fd3lyth.github.io%2Flunar_glow%2Fquiz.html) | ![screenshot](documentation/html-validation-quiz.png) | Pass: No Errors |
| Add Blog | n/a | ![screenshot](documentation/html-validation-add-blog.png) | Duplicate IDs found, and fixed |
| Checkout | n/a | ![screenshot](documentation/html-validation-checkout.png) | Pass: No Errors |
| x | x | x | repeat for all remaining HTML files |

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**IMPORTANT**: Python/Jinja syntax in HTML

Python projects that use Jinja syntax, such as `{% for loops %}`, `{% url 'home' %}`, and `{{ variable|filter }}`
will not validate properly if you're copying/pasting into the HTML validator.

In order to properly validate these types of files, it's recommended to
[validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, pages that require a user to be logged-in and authenticated (CRUD functionality),
will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have
access to login to your pages.
In order to properly validate HTML pages with Jinja syntax for authenticated pages, follow these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fd3lyth.github.io%2Flunar_glow) | ![screenshot](documentation/css-validation-base.png) | Pass: No Errors |
| checkout.css | n/a | ![screenshot](documentation/css-validation-checkout.png) | Pass: No Errors |
| profile.css | n/a | ![screenshot](documentation/css-validation-profile.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/js-validation-stripe.png) | Undefined Stripe variable - external library |
| countryfield.js | ![screenshot](documentation/js-validation-countryfield.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Bag urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/bag/urls.py) | ![screenshot](documentation/py-validation-bag-urls.png) | Pass: No Errors |
| Bag views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/d3lyth/lunar_glow/main/profiles/models.py) | ![screenshot](documentation/py-validation-bag-views.png) | Pass: No Errors |
| Bag apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/bag/apps.py) | ![screenshot](documentation/py-validation-bag-apps.png) | Pass: No Errors |
| Bag bagtools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/py-validation-bag-bagtools.png) | Pass: No Errors |

| Checkout admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/admin.py) | ![screenshot](documentation/py-validation-checkout-admin.png) | Pass: No Errors |
| Checkout forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/forms.py) | ![screenshot](documentation/py-validation-checkout-forms.png) | Pass: No Errors |
| Checkout models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/models.py) | ![screenshot](documentation/py-validation-checkout-models.png) | Pass: No Errors |
| Checkout signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/signals.py) | ![screenshot](documentation/py-validation-checkout-signals.png) | Pass: No Errors |
| Checkout urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/urls.py) | ![screenshot](documentation/py-validation-checkout-urls.png) | Pass: No Errors |
| Checkout views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/views.py
) | ![screenshot](documentation/py-validation-checkout-views.png) | Pass: No Errors |
| Checkout webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/webhook_handler.py) | ![screenshot](documentation/py-validation-checkout-webhook_handler.png) | Pass: No Errors |
| Checkout webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/webhooks.py) | ![screenshot](documentation/py-validation-checkout-webhooks.png) | Error: Line too long |

| FAQs admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/faqs/admin.py) | ![screenshot](documentation/py-validation-faqs-admin.png) | Pass: No Errors |
| FAQs models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/faqs/models.py) | ![screenshot](documentation/py-validation-faqs-models.png) | Pass: No Errors |
| FAQs urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/faqs/urls.py) | ![screenshot](documentation/py-validation-faqs-urls.png) | Pass: No Errors |
| FAQs views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/faqs/views.py) | ![screenshot](documentation/py-validation-faqs-views.png) | Pass: No Errors |

| Home urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/home/urls.py) | ![screenshot](documentation/py-validation-home-urls.png) | Pass: No Errors |
| Home views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/home/views.py) | ![screenshot](documentation/py-validation-home-views.png) | Pass: No Errors |

| Lunar Glow settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/lunar_glow/settings.py) | ![screenshot](documentation/py-validation-lunarglow-settings.png) | Pass: No Errors |
| Lunar Glow urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/lunar_glow/urls.py) | ![screenshot](documentation/py-validation-lunarglow-urls.png) | Pass: No Errors |

| Newsletter admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/admin.py) | ![screenshot](documentation/py-validation-newsletter-admin.png) | Pass: No Errors |
| Newsletter forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/forms.py) | ![screenshot](documentation/py-validation-newsletter-forms.png) | Pass: No Errors |
| Newsletter models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/models.py) | ![screenshot](documentation/py-validation-newsletter-models.png) | Pass: No Errors |
| Newsletter urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/urls.py) | ![screenshot](documentation/py-validation-newsletter-urls.png) | Pass: No Errors |
| Newsletter views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/views.py) | ![screenshot](documentation/py-validation-newsletter-views.png) | Pass: No Errors |

| Products admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/admin.py) | ![screenshot](documentation/py-validation-products-admin.png) | Pass: No Errors |
| Products forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/forms.py) | ![screenshot](documentation/py-validation-products-forms.png) | Pass: No Errors |
| Products models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/models.py) | ![screenshot](documentation/py-validation-products-models.png) | Pass: No Errors |
| Products urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/urls.py) | ![screenshot](documentation/py-validation-products-urls.png) | Pass: No Errors |
| Products views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/views.py) | ![screenshot](documentation/py-validation-products-views.png) | Pass: No Errors |
| Products widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/widgets.py) | ![screenshot](documentation/py-validation-products-widgets.png) | Pass: No Errors |

| Profiles forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/profiles/forms.py) | ![screenshot](documentation/py-validation-profiles-forms.png) | Pass: No Errors |
| Profiles models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/profiles/models.py) | ![screenshot](documentation/py-validation-profiles-models.png) | Pass: No Errors |
| Profiles urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/profiles/urls.py) | ![screenshot](documentation/py-validation-profiles-urls.png) | Pass: No Errors |
| Profiles views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/profiles/views.py) | ![screenshot](documentation/py-validation-profiles-views.png) | Pass: No Errors |

| Scent Profile admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/scentprofile/admin.py) | ![screenshot](documentation/py-validation-scentprofile-admin.png) | Pass: No Errors |
| Scent Profile models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/scentprofile/models.py) | ![screenshot](documentation/py-validation-scentprofile-models.png) | Pass: No Errors |
| Scent Profile urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/scentprofile/urls.py) | ![screenshot](documentation/py-validation-scentprofile-urls.png) | Pass: No Errors |
| Scent Profile views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/scentprofile/views.py) | ![screenshot](documentation/py-validation-scentprofile-views.png) | Pass: No Errors |

| Root Level custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/custom_storages.py) | ![screenshot](documentation/py-validation-rootlevel-custom-storages.png) | Pass: No Errors |
| Root Level manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/manage.py) | ![screenshot](documentation/py-validation-rootlevel-manage.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.
The browsers tested include:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)
🛑🛑🛑🛑🛑
| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-about.png) | ![screenshot](documentation/browser-chrome-contact.png) | ![screenshot](documentation/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-firefox-about.png) | ![screenshot](documentation/browser-firefox-contact.png) | ![screenshot](documentation/browser-firefox-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browser-edge-home.png) | ![screenshot](documentation/browser-edge-about.png) | ![screenshot](documentation/browser-chrome-edge.png) | ![screenshot](documentation/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browser-safari-home.png) | ![screenshot](documentation/browser-safari-about.png) | ![screenshot](documentation/browser-safari-contact.png) | ![screenshot](documentation/browser-safari-etc.png) | Minor CSS differences |
| Brave | ![screenshot](documentation/browser-brave-home.png) | ![screenshot](documentation/browser-brave-about.png) | ![screenshot](documentation/browser-brave-contact.png) | ![screenshot](documentation/browser-brave-etc.png) | Works as expected |
| Opera | ![screenshot](documentation/browser-opera-home.png) | ![screenshot](documentation/browser-opera-about.png) | ![screenshot](documentation/browser-opera-contact.png) | ![screenshot](documentation/browser-opera-etc.png) | Minor differences |
🛑🛑🛑🛑🛑

## Responsiveness

🛑🛑🛑🛑🛑
I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-about.png) | ![screenshot](documentation/responsive-mobile-contact.png) | ![screenshot](documentation/responsive-mobile-etc.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-about.png) | ![screenshot](documentation/responsive-tablet-contact.png) | ![screenshot](documentation/responsive-tablet-etc.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-about.png) | ![screenshot](documentation/responsive-desktop-contact.png) | ![screenshot](documentation/responsive-desktop-etc.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xl-home.png) | ![screenshot](documentation/responsive-xl-about.png) | ![screenshot](documentation/responsive-xl-contact.png) | ![screenshot](documentation/responsive-xl-etc.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsive-4k-home.png) | ![screenshot](documentation/responsive-4k-about.png) | ![screenshot](documentation/responsive-4k-contact.png) | ![screenshot](documentation/responsive-4k-etc.png) | Noticeable scaling issues |
| Google Pixel 7 Pro | ![screenshot](documentation/responsive-pixel-home.png) | ![screenshot](documentation/responsive-pixel-about.png) | ![screenshot](documentation/responsive-pixel-contact.png) | ![screenshot](documentation/responsive-pixel-etc.png) | Works as expected |
| iPhone 14 | ![screenshot](documentation/responsive-iphone-home.png) | ![screenshot](documentation/responsive-iphone-about.png) | ![screenshot](documentation/responsive-iphone-contact.png) | ![screenshot](documentation/responsive-iphone-etc.png) | Works as expected |

## Lighthouse Audit

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Don't just test the home page (unless it's a single-page application).
Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

## User Story Testing

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

## Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

## Unfixed Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

There are no remaining bugs that I am aware of.
