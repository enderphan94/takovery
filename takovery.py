import argparse
import asyncio
import aiohttp
import dns.resolver
import subprocess
import json
import csv
import re

FINGERPRINTS_URL = "https://raw.githubusercontent.com/EdOverflow/can-i-take-over-xyz/master/fingerprints.json"

def load_fingerprints():
    print("-->>>> Author: Ender Phan")
    print("https://github.com/enderphan94/takovery")
    print("\n")
    """Load fingerprints dynamically from FINGERPRINTS_URL or fallback to static fingerprints."""
    static_fingerprints = [
  {
    "cname": [
      "elasticbeanstalk.com"
    ],
    "discussion": "[Issue #194](https://github.com/EdOverflow/can-i-take-over-xyz/issues/194)",
    "documentation": "",
    "fingerprint": "NXDOMAIN",
    "service": "AWS/Elastic Beanstalk"
  },
  {
    "cname": [
      "elb.amazonaws.com"
    ],
    "discussion": "[Issue #137](https://github.com/EdOverflow/can-i-take-over-xyz/issues/137)",
    "documentation": "",
    "fingerprint": "NXDOMAIN",
    "service": "AWS/Load Balancer (ELB)",
    "status": "Not vulnerable"
  },
  {
    "cname": [
      "s3.amazonaws.com"
    ],
    "discussion": "[Issue #36](https://github.com/EdOverflow/can-i-take-over-xyz/issues/36)",
    "documentation": "",
    "fingerprint": "The specified bucket does not exist",
    "service": "AWS/S3"
  },
  {
    "cname": [],
    "discussion": "[Issue #103](https://github.com/EdOverflow/can-i-take-over-xyz/issues/103)",
    "documentation": "",
    "fingerprint": "Web Site Not Found",
    "service": "Acquia",
    "status": "Not vulnerable"
  },
  {
    "cname": [
      "agilecrm.com"
    ],
    "discussion": "[Issue #145](https://github.com/EdOverflow/can-i-take-over-xyz/issues/145)",
    "documentation": "",
    "fingerprint": "Sorry, this page is no longer available.",
    "service": "Agile CRM"
  },
  {
    "cname": [
      "airee.ru"
    ],
    "discussion": "[Issue #104](https://github.com/EdOverflow/can-i-take-over-xyz/issues/104)",
    "documentation": "",
    "fingerprint": "Ошибка 402. Сервис Айри.рф не оплачен",
    "service": "Airee.ru"
  },
  {
    "cname": [],
    "discussion": "[Issue #13](https://github.com/EdOverflow/can-i-take-over-xyz/issues/13)",
    "documentation": "",
    "fingerprint": "",
    "service": "Akamai",
    "status": "Not vulnerable"
  },
  {
    "cname": [
      "animaapp.io"
    ],
    "discussion": "[Issue #126](https://github.com/EdOverflow/can-i-take-over-xyz/issues/126)",
    "documentation": "[Anima Documentation](https://docs.animaapp.com/v1/launchpad/08-custom-domain.html)",
    "fingerprint": "The page you were looking for does not exist.",
    "service": "Anima"
  },
  {
    "cname": [
      "bitbucket.io"
    ],
    "discussion": "[Issue #97](https://github.com/EdOverflow/can-i-take-over-xyz/issues/97)",
    "documentation": "",
    "fingerprint": "Repository not found",
    "service": "Bitbucket"
  },
  {
    "cname": [],
    "discussion": "[Issue #275](https://github.com/EdOverflow/can-i-take-over-xyz/issues/275)",
    "documentation": "[Support Page](https://help.campaignmonitor.com/custom-domain-names)",
    "fingerprint": "Trying to access your account?",
    "service": "Campaign Monitor"
  },
  {
    "cname": [],
    "discussion": "[Issue #114](https://github.com/EdOverflow/can-i-take-over-xyz/issues/114)",
    "documentation": "",
    "fingerprint": "Company Not Found` `There is no such company. Did you enter the right URL?",
    "service": "Canny"
  },
  {
    "cname": [],
    "discussion": "[Issue #152](https://github.com/EdOverflow/can-i-take-over-xyz/issues/152)",
    "documentation": "[Cargo Support Page](https://support.2.cargocollective.com/Using-a-Third-Party-Domain)",
    "fingerprint": "404 Not Found",
    "service": "Cargo Collective"
  },
  {
    "cname": [],
    "discussion": "[Issue #29](https://github.com/EdOverflow/can-i-take-over-xyz/issues/29)",
    "documentation": "[Domain Security on Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/continually-enhancing-domain-security-on-amazon-cloudfront/)",
    "fingerprint": "ViewerCertificateException",
    "service": "Cloudfront",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #9](https://github.com/EdOverflow/can-i-take-over-xyz/issues/9)",
    "documentation": "",
    "fingerprint": "Please try again or try Desk.com free for 14 days.",
    "service": "Desk",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "",
    "documentation": "",
    "fingerprint": "Domain uses DO name servers with no records in DO.",
    "service": "Digital Ocean"
  },
  {
    "cname": [
      "trydiscourse.com"
    ],
    "discussion": "[Issue #49](https://github.com/EdOverflow/can-i-take-over-xyz/issues/49)",
    "documentation": "[Hackerone](https://hackerone.com/reports/264494)",
    "fingerprint": "NXDOMAIN",
    "service": "Discourse"
  },
  {
    "cname": [],
    "discussion": "[Issue #153](https://github.com/EdOverflow/can-i-take-over-xyz/issues/153) [Issue #5](https://github.com/shifa123/Can-I-take-over-xyz-v2/issues/5v)",
    "documentation": "",
    "fingerprint": "Site Not Found Well, this is awkward. The site you're looking for is not here.",
    "service": "Dreamhost",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #22](https://github.com/EdOverflow/can-i-take-over-xyz/issues/22)",
    "documentation": "",
    "fingerprint": "Fastly error: unknown domain:",
    "service": "Fastly",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #80](https://github.com/EdOverflow/can-i-take-over-xyz/issues/80)",
    "documentation": "",
    "fingerprint": "The feed has not been found.",
    "service": "Feedpress",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #128](https://github.com/EdOverflow/can-i-take-over-xyz/issues/128)",
    "documentation": "",
    "fingerprint": "",
    "service": "Firebase",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #101](https://github.com/EdOverflow/can-i-take-over-xyz/issues/101)",
    "documentation": "",
    "fingerprint": "404 Not Found",
    "service": "Fly.io",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #214](https://github.com/EdOverflow/can-i-take-over-xyz/issues/214)",
    "documentation": "[Freshdesk Support Page](https://support.freshdesk.com/support/solutions/articles/37590-using-a-vanity-support-url-and-pointing-the-cname)",
    "fingerprint": "We couldn't find servicedesk.victim.tld Maybe this is still fresh! You can claim it now at http://www.freshservice.com/signup",
    "service": "Freshdesk",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #170](https://github.com/EdOverflow/can-i-take-over-xyz/issues/170)",
    "documentation": "",
    "fingerprint": "404 - Page Not Found` `Oops… looks like you got lost",
    "service": "Frontify",
    "status": "Edge case"
  },
  {
    "cname": [
      "furyns.com"
    ],
    "discussion": "[Issue #154](https://github.com/EdOverflow/can-i-take-over-xyz/issues/154)",
    "documentation": "[Article](https://khaledibnalwalid.wordpress.com/2020/06/25/gemfury-subdomain-takeover/)",
    "fingerprint": "404: This page could not be found.",
    "service": "Gemfury"
  },
  {
    "cname": [],
    "discussion": "[Issue #235](https://github.com/EdOverflow/can-i-take-over-xyz/issues/235)",
    "documentation": "",
    "fingerprint": "With GetResponse Landing Pages, lead generation has never been easier",
    "service": "Getresponse"
  },
  {
    "cname": [
      "ghost.io"
    ],
    "discussion": "[Issue #89](https://github.com/EdOverflow/can-i-take-over-xyz/issues/89)",
    "documentation": "",
    "fingerprint": "Site unavailable\\.&#124;Failed to resolve DNS path for this host",
    "service": "Ghost"
  },
  {
    "cname": [],
    "discussion": "[Issue #37](https://github.com/EdOverflow/can-i-take-over-xyz/issues/37) [Issue #68](https://github.com/EdOverflow/can-i-take-over-xyz/issues/68)",
    "documentation": "",
    "fingerprint": "There isn't a GitHub Pages site here.",
    "service": "Github",
    "status": "Edge case"
  },
  {
    "cname": [],
    "discussion": "[HackerOne #312118](https://hackerone.com/reports/312118)",
    "documentation": "",
    "fingerprint": "",
    "service": "Gitlab",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "",
    "documentation": "",
    "fingerprint": "<?xml version='1.0' encoding='UTF-8'?><Error><Code>NoSuchBucket</Code><Message>The specified bucket does not exist.</Message></Error>",
    "service": "Google Cloud Storage",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #277](https://github.com/EdOverflow/can-i-take-over-xyz/issues/277)",
    "documentation": "[Google Support](https://support.google.com/webmasters/answer/9008080?visit_id=637981741431097680-3818919062&rd=2)",
    "fingerprint": "The requested URL was not found on this server. That’s all we know.",
    "service": "Google Sites",
    "status": "Not vulnerable"
  },
  {
    "cname": [
      "hatenablog.com"
    ],
    "discussion": "",
    "documentation": "",
    "fingerprint": "404 Blog is not found",
    "service": "HatenaBlog"
  },
  {
    "cname": [
      "helpjuice.com"
    ],
    "discussion": "",
    "documentation": "[Help Juice Support Page](https://help.helpjuice.com/en_US/using-your-custom-domain/how-to-set-up-a-custom-domain)",
    "fingerprint": "We could not find what you're looking for.",
    "service": "Help Juice"
  },
  {
    "cname": [
      "helpscoutdocs.com"
    ],
    "discussion": "",
    "documentation": "[HelpScout Docs](https://docs.helpscout.net/article/42-setup-custom-domain)",
    "fingerprint": "No settings were found for this company:",
    "service": "Help Scout"
  },
  {
    "cname": [
      "helprace.com"
    ],
    "discussion": "[Issue #115](https://github.com/EdOverflow/can-i-take-over-xyz/issues/115)",
    "documentation": "",
    "fingerprint": "HTTP_STATUS=301",
    "http_status": 301,
    "service": "Helprace"
  },
  {
    "cname": [],
    "discussion": "[Issue #38](https://github.com/EdOverflow/can-i-take-over-xyz/issues/38)",
    "documentation": "",
    "fingerprint": "No such app",
    "service": "Heroku",
    "status": "Edge case"
  },
  {
    "cname": [],
    "discussion": "[Issue #59](https://github.com/EdOverflow/can-i-take-over-xyz/issues/59)",
    "documentation": "",
    "fingerprint": "This page isn't available",
    "service": "HubSpot",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #73](https://github.com/EdOverflow/can-i-take-over-xyz/issues/73)",
    "documentation": "",
    "fingerprint": "",
    "service": "Instapage",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #69](https://github.com/EdOverflow/can-i-take-over-xyz/issues/69)",
    "documentation": "[Help center](https://www.intercom.com/help/)",
    "fingerprint": "Uh oh. That page doesn't exist.",
    "service": "Intercom",
    "status": "Edge case"
  },
  {
    "cname": [
      "youtrack.cloud"
    ],
    "discussion": "[PR #107](https://github.com/EdOverflow/can-i-take-over-xyz/pull/107)",
    "documentation": "[YouTrack InCloud Help Page](https://www.jetbrains.com/help/youtrack/incloud/Domain-Settings.html)",
    "fingerprint": "is not a registered InCloud YouTrack",
    "service": "JetBrains"
  },
  {
    "cname": [],
    "discussion": "[Issue #112](https://github.com/EdOverflow/can-i-take-over-xyz/issues/112)",
    "documentation": "",
    "fingerprint": "",
    "service": "Key CDN",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #48](https://github.com/EdOverflow/can-i-take-over-xyz/issues/48)",
    "documentation": "[kinsta-add-domain](https://kinsta.com/knowledgebase/add-domain/)",
    "fingerprint": "No Site For Domain",
    "service": "Kinsta",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #117](https://github.com/EdOverflow/can-i-take-over-xyz/issues/117)",
    "documentation": "",
    "fingerprint": "It looks like you’re lost...",
    "service": "Landingi",
    "status": "Edge case"
  },
  {
    "cname": [
      "launchrock.com"
    ],
    "discussion": "[Issue #74](https://github.com/EdOverflow/can-i-take-over-xyz/issues/74)",
    "documentation": "",
    "fingerprint": "HTTP_STATUS=500",
    "http_status": 500,
    "service": "LaunchRock"
  },
  {
    "cname": [],
    "discussion": "[Discussion #250](https://github.com/EdOverflow/can-i-take-over-xyz/discussions/250)",
    "documentation": "",
    "fingerprint": "We can't find that page It looks like you're trying to reach a page that was built by Mailchimp but is no longer active.",
    "service": "Mailchimp",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #14](https://github.com/EdOverflow/can-i-take-over-xyz/issues/14)",
    "documentation": "[HackerOne](https://hackerone.com/reports/275714)",
    "fingerprint": "Unrecognized domain",
    "service": "Mashery",
    "status": "Edge case"
  },
  {
    "cname": [
      "cloudapp.net",
      "cloudapp.azure.com",
      "azurewebsites.net",
      "blob.core.windows.net",
      "cloudapp.azure.com",
      "azure-api.net",
      "azurehdinsight.net",
      "azureedge.net",
      "azurecontainer.io",
      "database.windows.net",
      "azuredatalakestore.net",
      "search.windows.net",
      "azurecr.io",
      "redis.cache.windows.net",
      "azurehdinsight.net",
      "servicebus.windows.net",
      "visualstudio.com"
    ],
    "discussion": "[Issue #35](https://github.com/EdOverflow/can-i-take-over-xyz/issues/35)",
    "documentation": "",
    "fingerprint": "NXDOMAIN",
    "service": "Microsoft Azure"
  },
  {
    "cname": [],
    "discussion": "[Issue #40](https://github.com/EdOverflow/can-i-take-over-xyz/issues/40)",
    "documentation": "",
    "fingerprint": "Not Found - Request ID:",
    "service": "Netlify",
    "status": "Edge case"
  },
  {
    "cname": [
      "ngrok.io"
    ],
    "discussion": "[Issue #92](https://github.com/EdOverflow/can-i-take-over-xyz/issues/92)",
    "documentation": "[Ngrok Documentation](https://ngrok.com/docs#http-custom-domains)",
    "fingerprint": "Tunnel .*.ngrok.io not found",
    "service": "Ngrok"
  },
  {
    "cname": [],
    "discussion": "[Issue #24](https://github.com/EdOverflow/can-i-take-over-xyz/issues/24)",
    "documentation": "[Documentation](https://pantheon.io/docs/guides/domains/custom-domains) [Pantheon-Sub-takeover](https://medium.com/@hussain_0x3c/hostile-subdomain-takeover-using-pantheon-ebf4ab813111)",
    "fingerprint": "404 error unknown site!",
    "service": "Pantheon"
  },
  {
    "cname": [],
    "discussion": "[Issue #144](https://github.com/EdOverflow/can-i-take-over-xyz/issues/144)",
    "documentation": "[Support Page](https://help.pingdom.com/hc/en-us/articles/205386171-Public-Status-Page)",
    "fingerprint": "Sorry, couldn't find the status page",
    "service": "Pingdom"
  },
  {
    "cname": [
      "readme.io"
    ],
    "discussion": "[Issue #41](https://github.com/EdOverflow/can-i-take-over-xyz/issues/41)",
    "documentation": "",
    "fingerprint": "The creators of this project are still working on making everything perfect!",
    "service": "Readme.io"
  },
  {
    "cname": [],
    "discussion": "[Issue #160](https://github.com/EdOverflow/can-i-take-over-xyz/issues/160)",
    "documentation": "",
    "fingerprint": "The link you have followed or the URL that you entered does not exist.",
    "service": "Readthedocs"
  },
  {
    "cname": [],
    "discussion": "",
    "documentation": "",
    "fingerprint": "",
    "service": "Sendgrid",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #32](https://github.com/EdOverflow/can-i-take-over-xyz/issues/32) [Issue #46](https://github.com/EdOverflow/can-i-take-over-xyz/issues/46)",
    "documentation": "[Medium Article](https://medium.com/@thebuckhacker/how-to-do-55-000-subdomain-takeover-in-a-blink-of-an-eye-a94954c3fc75)",
    "fingerprint": "Sorry, this shop is currently unavailable.",
    "service": "Shopify",
    "status": "Edge case"
  },
  {
    "cname": [],
    "discussion": "[Issue #260](https://github.com/EdOverflow/can-i-take-over-xyz/issues/260)",
    "documentation": "",
    "fingerprint": "Link does not exist",
    "service": "Short.io"
  },
  {
    "cname": [
      "52.16.160.97"
    ],
    "discussion": "[Issue #139](https://github.com/EdOverflow/can-i-take-over-xyz/issues/139)",
    "documentation": "[Support Page](https://help.smartjobboard.com/en/articles/1269655-connecting-a-custom-domain-name)",
    "fingerprint": "This job board website is either expired or its domain name is invalid.",
    "service": "SmartJobBoard"
  },
  {
    "cname": [],
    "discussion": "[Issue #67](https://github.com/EdOverflow/can-i-take-over-xyz/issues/67)",
    "documentation": "",
    "fingerprint": "Domain is not configured",
    "service": "Smartling",
    "status": "Edge case"
  },
  {
    "cname": [],
    "discussion": "[Issue #60](https://github.com/EdOverflow/can-i-take-over-xyz/issues/60)",
    "documentation": "",
    "fingerprint": "",
    "service": "Smugsmug"
  },
  {
    "cname": [],
    "discussion": "",
    "documentation": "",
    "fingerprint": "",
    "service": "Squarespace",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "Status page pushed a DNS verification in order to prevent malicious takeovers what they mentioned in [This Doc](https://support.atlassian.com/statuspage/docs/configure-your-dns/) [PR #105](https://github.com/EdOverflow/can-i-take-over-xyz/pull/105) [PR #171](https://github.com/EdOverflow/can-i-take-over-xyz/pull/171)",
    "documentation": "[Statuspage documentation](https://help.statuspage.io/knowledge_base/topics/domain-ownership)",
    "fingerprint": "",
    "service": "Statuspage",
    "status": "Not vulnerable"
  },
  {
    "cname": [
      "s.strikinglydns.com"
    ],
    "discussion": "[Issue #58](https://github.com/EdOverflow/can-i-take-over-xyz/issues/58)",
    "documentation": "[Strikingly-Sub-takeover](https://medium.com/@sherif0x00/takeover-subdomains-pointing-to-strikingly-5e67df80cdfd)",
    "fingerprint": "PAGE NOT FOUND.",
    "service": "Strikingly"
  },
  {
    "cname": [
      "na-west1.surge.sh"
    ],
    "discussion": "[Issue #198](https://github.com/EdOverflow/can-i-take-over-xyz/issues/198)",
    "documentation": "[Surge Documentation](https://surge.sh/help/adding-a-custom-domain)",
    "fingerprint": "project not found",
    "service": "Surge.sh"
  },
  {
    "cname": [
      "surveysparrow.com"
    ],
    "discussion": "[Issue #281](https://github.com/EdOverflow/can-i-take-over-xyz/issues/281)",
    "documentation": "[Custom domain](https://help.surveysparrow.com/custom-domain)",
    "fingerprint": "Account not found.",
    "service": "SurveySparrow"
  },
  {
    "cname": [],
    "discussion": "[Issue #155](https://github.com/EdOverflow/can-i-take-over-xyz/issues/155) [PR #20](https://github.com/EdOverflow/can-i-take-over-xyz/pull/20)",
    "documentation": "",
    "fingerprint": "Please renew your subscription",
    "service": "Tilda",
    "status": "Edge case"
  },
  {
    "cname": [],
    "discussion": "[Issue #240](https://github.com/EdOverflow/can-i-take-over-xyz/issues/240)",
    "documentation": "[Tumblr Custom Domains](https://www.tumblr.com/docs/en/custom_domains)",
    "fingerprint": "Whatever you were looking for doesn't currently exist at this address",
    "service": "Tumblr",
    "status": "Edge case"
  },
  {
    "cname": [
      "read.uberflip.com"
    ],
    "discussion": "[Issue #150](https://github.com/EdOverflow/can-i-take-over-xyz/issues/150)",
    "documentation": "[Uberflip Documentation](https://help.uberflip.com/hc/en-us/articles/360018786372-Custom-Domain-Set-up-Your-Hub-on-a-Subdomain)",
    "fingerprint": "The URL you've accessed does not provide a hub.",
    "service": "Uberflip"
  },
  {
    "cname": [],
    "discussion": "[Issue #11](https://github.com/EdOverflow/can-i-take-over-xyz/issues/11)",
    "documentation": "",
    "fingerprint": "The requested URL was not found on this server.",
    "service": "Unbounce",
    "status": "Not vulnerable"
  },
  {
    "cname": [
      "stats.uptimerobot.com"
    ],
    "discussion": "[Issue #45](https://github.com/EdOverflow/can-i-take-over-xyz/issues/45)",
    "documentation": "[Uptimerobot-Sub-takeover](https://exploit.linuxsec.org/uptimerobot-com-custom-domain-subdomain-takeover/)",
    "fingerprint": "page not found",
    "service": "Uptimerobot"
  },
  {
    "cname": [],
    "discussion": "[Issue #163](https://github.com/EdOverflow/can-i-take-over-xyz/issues/163)",
    "documentation": "",
    "fingerprint": "This UserVoice subdomain is currently available!",
    "service": "UserVoice",
    "status": "Not vulnerable"
  },
  {
    "cname": [
      "https://nonexistent-example.vercel.com/"
    ],
    "discussion": "[Issue #183](https://github.com/EdOverflow/can-i-take-over-xyz/issues/183)",
    "documentation": "[Adding & Configuring a Custom Domain](https://vercel.com/docs/concepts/projects/domains/add-a-domain)",
    "fingerprint": "DEPLOYMENT_NOT_FOUND.",
    "service": "Vercel",
    "status": "Edge case"
  },
  {
    "cname": [],
    "discussion": "",
    "documentation": "",
    "fingerprint": "",
    "service": "WP Engine",
    "status": "Not vulnerable"
  },
  {
    "cname": [],
    "discussion": "[Issue #44](https://github.com/EdOverflow/can-i-take-over-xyz/issues/44)",
    "documentation": "[forum webflow](https://forum.webflow.com/t/hosting-a-subdomain-on-webflow/59201)",
    "fingerprint": "The page you are looking for doesn't exist or has been moved.",
    "service": "Webflow",
    "status": "Edge case"
  },
  {
    "cname": [],
    "discussion": "[Issue #231](https://github.com/EdOverflow/can-i-take-over-xyz/issues/231)",
    "documentation": "",
    "fingerprint": "Looks Like This Domain Isn't Connected To A Website Yet!",
    "service": "Wix",
    "status": "Edge case"
  },
  {
    "cname": [
      "wordpress.com"
    ],
    "discussion": "[PR #176](https://github.com/EdOverflow/can-i-take-over-xyz/pull/176)",
    "documentation": "",
    "fingerprint": "Do you want to register .*.wordpress.com?",
    "service": "Wordpress"
  },
  {
    "cname": [
      "worksites.net",
      "69.164.223.206"
    ],
    "discussion": "[Issue #142](https://github.com/EdOverflow/can-i-take-over-xyz/issues/142)",
    "documentation": "",
    "fingerprint": "Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist.",
    "service": "Worksites"
  },
  {
    "cname": [],
    "discussion": "[Issue #23](https://github.com/EdOverflow/can-i-take-over-xyz/issues/23)",
    "documentation": "[Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203664356-Changing-the-address-of-your-Help-Center-subdomain-host-mapping-)",
    "fingerprint": "Help Center Closed",
    "service": "Zendesk",
    "status": "Not vulnerable"
  }
]
    try:
        response = subprocess.run(
            ["curl", "-s", FINGERPRINTS_URL],
            stdout=subprocess.PIPE,
            text=True,
        )
        if response.stdout:
            fingerprints = json.loads(response.stdout)
            processed_fingerprints = [
                {
                    "service": entry.get("service"),
                    "cname": entry.get("cname", []),
                    "fingerprint": entry.get("fingerprint"),
                }
                for entry in fingerprints
            ]
            print("[INFO] Fingerprints successfully loaded from remote source.")
            return processed_fingerprints
    except Exception as e:
        print(f"[ERROR] Failed to load fingerprints dynamically: {e}")

    # Fallback to static fingerprints
    print("[INFO] Using static fingerprints.")
    return static_fingerprints

FINGERPRINTS = load_fingerprints()

REGEX_PATTERNS = {
    "AWS/S3": r"The specified bucket does not exist",
    "BitBucket": r"Repository not found",
    "Github": r"There isn't a Github Pages site here\.|a Github Pages site here",
    "Shopify": r"Sorry, this shop is currently unavailable\.",
    "Fastly": r"Fastly error: unknown domain:",
    "Ghost": r"The thing you were looking for is no longer here, or never was",
    "Heroku": r"no-such-app.html|<title>no such app</title>|herokucdn.com/error-pages/no-such-app.html|No such app",
    "Pantheon": r"The gods are wise, but do not know of the site which you seek|404 error unknown site",
    "Tumbler": r"Whatever you were looking for doesn't currently exist at this address\.",
    "Wordpress": r"Do you want to register",
    "TeamWork": r"Oops - We didn't find your site\.",
    "Helpjuice": r"We could not find what you're looking for\.",
    "Helpscout": r"No settings were found for this company:",
    "Cargo": r"<title>404 &mdash; File not found</title>",
    "Uservoice": r"This UserVoice subdomain is currently available",
    "Surge.sh": r"project not found",
    "Intercom": r"This page is reserved for artistic dogs\.|Uh oh\. That page doesn't exist</h1>",
    "Webflow": r"<p class=\"description\">The page you are looking for doesn't exist or has been moved\.</p>|The page you are looking for doesn't exist or has been moved",
    "Kajabi": r"<h1>The page you were looking for doesn't exist\.</h1>",
    "Thinkific": r"You may have mistyped the address or the page may have moved\.",
    "Tave": r"<h1>Error 404: Page Not Found</h1>",
    "Wishpond": r"<h1>https://www.wishpond.com/404\?campaign=true",
    "Aftership": r"Oops\.</h2><p class=\"text-muted text-tight\">The page you're looking for doesn't exist\.",
    "Aha": r"There is no portal here \.\.\. sending you back to Aha!",
    "Tictail": r"to target URL: <a href=\"https://tictail.com|Start selling on Tictail\.",
    "Brightcove": r"<p class=\"bc-gallery-error-code\">Error Code: 404</p>",
    "Bigcartel": r"<h1>Oops! We couldn’t find that page\.</h1>",
    "ActiveCampaign": r"alt=\"LIGHTTPD - fly light\.\"",
    "Campaignmonitor": r"Double check the URL or <a href=\"mailto:help@createsend.com|Trying to access your account",
    "Acquia": r"The site you are looking for could not be found\.|If you are an Acquia Cloud customer and expect to see your site at this address|Web Site Not Found",
    "Proposify": r"If you need immediate assistance, please contact <a href=\"mailto:support@proposify.biz",
    "Simplebooklet": r"We can't find this <a href=\"https://simplebooklet.com",
    "GetResponse": r"With GetResponse Landing Pages, lead generation has never been easier",
    "Vend": r"Looks like you've traveled too far into cyberspace\.",
    "Jetbrains": r"is not a registered InCloud YouTrack\.",
    "Smartling": r"Domain is not configured",
    "Pingdom": r"pingdom|Sorry, couldn't find the status page",
    "Tilda": r"Domain has been assigned|Please renew your subscription",
    "Surveygizmo": r"data-html-name",
    "Mashery": r"Unrecognized domain <strong>|Unrecognized domain",
    "Divio": r"Application not responding",
    "feedpress": r"The feed has not been found\.",
    "Readme.io": r"Project doesn't exist... yet!",
    "statuspage": r"You are being <a href='https>",
    "zendesk": r"Help Center Closed",
    "worksites.net": r"Hello! Sorry, but the webs>",
    "Agile CRM": r"this page is no longer available",
    "Anima": r"try refreshing in a minute|this is your website and you've just created it",
    "Fly.io": r"404 Not Found",
    "Gemfury": r"This page could not be found",
    "HatenaBlog": r"404 Blog is not found",
    "Kinsta": r"No Site For Domain",
    "LaunchRock": r"It looks like you may have taken a wrong turn somewhere|worry...it happens to all of us",
    "Ngrok": r"ngrok.io not found",
    "SmartJobBoard": r"This job board website is either expired or its domain name is invalid",
    "Strikingly": r"page not found",
    "Tumblr": r"Whatever you were looking for doesn't currently exist at this address",
    "Uberflip": r"hub domain, The URL you've accessed does not provide a hub",
    "Unbounce": r"The requested URL was not found on this server",
    "Uptimerobot": r"page not found",
}


async def fetch_url(session, url):
    """Fetch HTTP response for a given URL."""
    try:
        async with session.get(url, timeout=5) as response:
            return await response.text()
    except Exception as e:
        return str(e)

def match_regex(content):
    """Check HTTP response content against regex patterns."""
    for service, pattern in REGEX_PATTERNS.items():
        if re.search(pattern, content, re.IGNORECASE):
            return service, pattern
    return None, None

def get_cname_with_dig(subdomain):
    """Fetch CNAME record using dig."""
    try:
        result = subprocess.run(
            ["dig", subdomain, "CNAME", "+short"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.stdout.strip() if result.stdout.strip() else None
    except Exception as e:
        print(f"[ERROR] Failed to fetch CNAME using dig for {subdomain}: {e}")
        return None

def get_cname_with_resolver(subdomain):
    """Fetch CNAME record using dns.resolver."""
    try:
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        return str(answers[0].target)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return None
    except Exception as e:
        print(f"[ERROR] DNS resolution failed for {subdomain} with dns.resolver: {e}")
        return None

def check_cname_against_fingerprints(resolved_cname):
    """Check if resolved CNAME matches any known vulnerable CNAME."""
    for entry in FINGERPRINTS:
        for known_cname in entry.get("cname", []):
            # Compare if the resolved CNAME matches or ends with a known vulnerable CNAME
            if resolved_cname and resolved_cname.endswith(known_cname):
                return entry["service"]
    return None

def check_http_content_against_fingerprints(content):
    """Check if HTTP response matches any known vulnerable fingerprint."""
    for entry in FINGERPRINTS:
        fingerprint = entry.get("fingerprint")
        if fingerprint and re.search(fingerprint, content, re.IGNORECASE):
            return entry["service"]
    return None

async def check_subdomain(subdomain):
    """Check subdomain for takeover vulnerabilities."""
    cname_resolver = get_cname_with_resolver(subdomain)
    cname_dig = get_cname_with_dig(subdomain)

    result = {
        "subdomain": subdomain,
        "cname_resolver": cname_resolver or "No CNAME (dns.resolver)",
        "cname_dig": cname_dig or "No CNAME (dig)",
        "org_name": "",
        "details": "",
        "vulnerable": False,
    }

    resolved_cname = cname_resolver or cname_dig
    if resolved_cname:
        # Check resolved CNAME against known vulnerable CNAMEs
        service = check_cname_against_fingerprints(resolved_cname)
        if service:
            result["vulnerable"] = True
            result["details"] = f"Resolved CNAME matches a known vulnerable service ({service})."
            return result

    # Perform WHOIS lookup for OrgName
    try:
        process = subprocess.run(
            ["whois", subdomain],
            stdout=subprocess.PIPE,
            text=True,
        )
        for line in process.stdout.splitlines():
            if "OrgName" in line:
                result["org_name"] = line.split(":")[1].strip()
                break
    except Exception as e:
        print(f"[ERROR] Failed to fetch OrgName for {subdomain}: {e}")

    # Check HTTP response content using both fingerprints and regex
    if not result["vulnerable"]:
        async with aiohttp.ClientSession() as session:
            html = await fetch_url(session, f"http://{subdomain}")
            
            # Check against fingerprints
            service_from_fingerprints = check_http_content_against_fingerprints(html)
            
            # Check against regex patterns
            service_from_regex, pattern = match_regex(html)
            
            # If either matches, mark as vulnerable
            if service_from_fingerprints:
                result["vulnerable"] = True
                result["details"] = f"HTTP response matches a known vulnerable service ({service_from_fingerprints})."
            elif service_from_regex:
                result["vulnerable"] = True
                result["details"] = f"HTTP response matches pattern '{pattern}' for service ({service_from_regex})."

    # Output results
    prefix = "[VULNERABLE]" if result["vulnerable"] else "[INFO]"
    print(f"\n{prefix} https://{result['subdomain']}:")
    print(f"CNAME (dns.resolver): {result['cname_resolver']}")
    print(f"CNAME (dig): {result['cname_dig']}")
    print(f"OrgName: {result['org_name']}")
    print(f"Details: {result['details']}")
    print("-" * 40)
    return result

async def process_domains(domains, output_format):
    """Process a list of domains asynchronously."""
    results = []
    vulnerable_domains = []
    tasks = [check_subdomain(domain) for domain in domains]
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

        if result["vulnerable"]:
            vulnerable_domains.append(result["subdomain"])

    save_results(results, output_format)

    print(f"\n[INFO] {len(vulnerable_domains)} vulnerable subdomains found.")
    if vulnerable_domains:
        print("[INFO] Vulnerable domains:")
        for domain in vulnerable_domains:
            print(f"- {domain}")

def save_results(results, output_format):
    """Save results to the specified output format."""
    if output_format == "json":
        with open("results.json", "w") as f:
            json.dump(results, f, indent=4)
    elif output_format == "csv":
        with open("results.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["subdomain", "cname_resolver", "cname_dig", "org_name", "details", "vulnerable"])
            writer.writeheader()
            writer.writerows(results)
    else:
        with open("results.txt", "w") as f:
            for result in results:
                f.write(
                    f"{result['subdomain']}\n"
                    f"CNAME (dns.resolver): {result['cname_resolver']}\n"
                    f"CNAME (dig): {result['cname_dig']}\n"
                    f"OrgName: {result['org_name']}\n"
                    f"Details: {result['details']}\n"
                    f"{'-'*40}\n"
                )

def parse_arguments():
    parser = argparse.ArgumentParser(description="Check subdomains for takeover vulnerabilities.")
    parser.add_argument("-d", "--domain", help="Single domain to check.")
    parser.add_argument("-iL", "--input_list", help="Path to the file containing the list of domains.")
    parser.add_argument("-o", "--output", default="results.txt", help="Output file format: txt, json, or csv.")
    return parser.parse_args()

def main():
    args = parse_arguments()

    domains = []
    if args.domain:
        domains = [args.domain]
    elif args.input_list:
        try:
            with open(args.input_list, "r") as f:
                domains = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"[ERROR] File {args.input_list} not found.")
            return
    else:
        print("[ERROR] Please provide either a single domain (-d) or a domain list (-iL).")
        return

    print(f"[INFO] Checking {len(domains)} subdomain(s) for takeover vulnerabilities...")
    asyncio.run(process_domains(domains, args.output))

if __name__ == "__main__":
    main()
