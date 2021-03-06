mappings = {
    "attributes": {
        "BITCOIN_ADDRESS": {
            "description": "A bitcoin address is an identifier of 26-35 alphanumeric characters, beginning with the number 1 or 3, that represents a possible destination for a bitcoin payment.",
            "misp-attribute": "btc",
            "multiple": True,
            "ui-priority": 1,
        },
        "CIDR_BLOCK": {
            "description": "CIDR (Classless Inter-Domain Routing) identifies a range of IP addresses, and was introduced as a way to allow more flexible allocation of Internet Protocol (IP) addresses than was possible with the original system of IP address classes.",
            "misp-attribute": "ip-src",
            "multiple": True,
            "ui-priority": 1,
        },
        "COMMENTS": {
            "description": "A space for additional comments.",
            "misp-attribute": "text",
            "multiple": True,
            "ui-priority": 1,
        },
        "CVE": {
            "description": "The Common Vulnerabilities and Exposures (CVE) system provides a reference-method for publicly known information-security vulnerabilities and exposures.",
            "misp-attribute": "vulnerability",
            "multiple": True,
            "ui-priority": 1,
        },
        "EMAIL_ADDRESS": {
            "description": "An email address is a unique identifier for an email account.",
            "misp-attribute": "email-src",
            "multiple": True,
            "ui-priority": 1,
        },
        "INDICATOR_SUMMARY": {
            "description": "Free text summary data related to an indicator. This should include a normalized score if one exists.",
            "misp-attribute": "text",
            "multiple": True,
            "ui-priority": 1,
        },
        "IP": {
            "description": "An Internet Protocol address (IP address) is a numerical label assigned to each device participating in a computer network that uses the Internet Protocol for communication.",
            "misp-attribute": "ip-dst",
            "multiple": True,
            "ui-priority": 1,
        },
        "MALWARE": {
            "description": "Names of software that are intended to damage or disable computers and computer systems.",
            "misp-attribute": "malware-type",
            "multiple": True,
            "ui-priority": 1,
        },
        "MD5": {
            "description": "The MD5 algorithm is a widely used hash function producing a 128-bit hash value.",
            "misp-attribute": "md5",
            "multiple": True,
            "ui-priority": 1,
        },
        "REGISTRY_KEY": {
            "description": "The registry is a hierarchical database that contains data that is critical for the operation of Windows and the applications and services that run on Windows.",
            "misp-attribute": "regkey",
            "multiple": True,
            "ui-priority": 1,
        },
        "REPORT_LINK": {
            "description": "A link to the TruSTAR report. Access may be restricted depending on user permissions.",
            "misp-attribute": "link",
            "multiple": True,
            "ui-priority": 1,
        },
        "SHA1": {
            "description": "SHA-1 (Secure Hash Algorithm 1) is a cryptographic hash function which takes an input and produces a 160-bit (20-byte) hash value known as a message digest - typically rendered as a hexadecimal number, 40 digits long. SHA-1 is prone to length extension attacks.",
            "misp-attribute": "sha1",
            "multiple": True,
            "ui-priority": 1,
        },
        "SHA256": {
            "description": "SHA-256 is a member of the SHA-2 cryptographic hash functions designed by the NSA, which are the successors to SHA-1. It is represented as a 64-character hexadecimal string.",
            "misp-attribute": "sha256",
            "multiple": True,
            "ui-priority": 1,
        },
        "SOFTWARE": {
            "description": "The name of a file on a filesystem.",
            "misp-attribute": "filename",
            "multiple": True,
            "ui-priority": 1,
        },
        "URL": {
            "description": "A Uniform Resource Locator (URL) is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.",
            "misp-attribute": "url",
            "multiple": True,
            "ui-priority": 1,
        },
        "THREAT_ACTOR": {
            "description": "A string identifying a threat actor.",
            "misp-attribute": "threat-actor",
            "multiple": True,
            "ui-priority": 1,
        },
    }
}
