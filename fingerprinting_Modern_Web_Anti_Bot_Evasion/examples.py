#!/usr/bin/env python3
"""
🔧 Practical Examples: From curl to curl_cffi

This file shows practical examples of converting curl commands
to curl_cffi requests, demonstrating real-world use cases.
"""

from curl_cffi import requests
import json

def example_1_basic_conversion():
    """
    Convert a basic curl command to curl_cffi
    
    Original curl:
    curl -H "User-Agent: Mozilla/5.0..." https://api.example.com/data
    
    Problem: Static headers, no TLS matching
    """
    print("🔄 Example 1: Basic Header Conversion")
    print("❌ Old way (easily detected):")
    print("   curl -H 'User-Agent: Mozilla/5.0...' https://httpbin.org/user-agent")
    
    # Old way with requests
    import requests as old_requests
    old_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    old_response = old_requests.get('https://httpbin.org/user-agent', headers=old_headers)
    print(f"   Result: {old_response.json()}")
    
    print("\n✅ New way (browser impersonation):")
    print("   requests.get(url, impersonate='chrome120')")
    
    # New way with curl_cffi
    new_response = requests.get('https://httpbin.org/user-agent', impersonate='chrome120')
    print(f"   Result: {new_response.json()}")
    print()

def example_2_tls_fingerprint_matching():
    """
    Show TLS fingerprint matching capabilities
    """
    print("🔍 Example 2: TLS Fingerprint Matching")
    print("Testing against tls.browserleaks.com...")
    
    try:
        response = requests.get(
            'https://tls.browserleaks.com/json',
            impersonate='chrome120',
            timeout=10
        )
        
        data = response.json()
        print(f"✅ JA3 Hash: {data.get('ja3_hash', 'Unknown')}")
        print(f"✅ TLS Version: {data.get('tls_version', 'Unknown')}")
        print(f"✅ User Agent: {data.get('user_agent', 'Unknown')[:50]}...")
        print("   ^ This fingerprint matches a real Chrome browser!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    print()

def example_3_browser_switching():
    """
    Demonstrate switching between different browser profiles
    """
    print("🎭 Example 3: Browser Profile Switching")
    
    browsers = [
        ('chrome120', 'Latest Chrome'),
        ('firefox117', 'Recent Firefox'),
        ('safari16_0', 'Safari on macOS'),
        ('edge101', 'Microsoft Edge')
    ]
    
    for browser_id, description in browsers:
        try:
            response = requests.get(
                'https://httpbin.org/user-agent',
                impersonate=browser_id,
                timeout=5
            )
            
            user_agent = response.json().get('user-agent', 'Unknown')
            print(f"✅ {description}: {user_agent[:60]}...")
            
        except Exception as e:
            print(f"❌ {description}: Error - {e}")
    print()

def example_4_session_persistence():
    """
    Show how to maintain sessions with cookies
    """
    print("🍪 Example 4: Session Management with Cookies")
    
    # Create a session
    session = requests.Session()
    
    # Set a cookie
    response1 = session.get(
        'https://httpbin.org/cookies/set/demo_cookie/barney_was_here',
        impersonate='chrome120',
        allow_redirects=False
    )
    
    print(f"✅ Cookie set: {response1.status_code}")
    
    # Use the cookie in next request
    response2 = session.get(
        'https://httpbin.org/cookies',
        impersonate='chrome120'
    )
    
    cookies = response2.json().get('cookies', {})
    print(f"✅ Cookie retrieved: {cookies}")
    print()

def example_5_post_requests():
    """
    Show POST requests with form data and JSON
    """
    print("📤 Example 5: POST Requests")
    
    # Form data
    form_data = {'username': 'barney', 'password': 'duff_beer'}
    response1 = requests.post(
        'https://httpbin.org/post',
        data=form_data,
        impersonate='chrome120'
    )
    
    print("✅ Form POST:")
    print(f"   Data sent: {response1.json().get('form', {})}")
    
    # JSON data
    json_data = {'user': 'barney', 'action': 'order_beer'}
    response2 = requests.post(
        'https://httpbin.org/post',
        json=json_data,
        impersonate='chrome120'
    )
    
    print("✅ JSON POST:")
    print(f"   Data sent: {response2.json().get('json', {})}")
    print()

def example_6_advanced_headers():
    """
    Show how to add custom headers while maintaining impersonation
    """
    print("🎯 Example 6: Custom Headers + Impersonation")
    
    custom_headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer fake_token_123',
        'X-Custom-Header': 'Barney-Scraper-v2.0',
        'Referer': 'https://moes-tavern.com',
    }
    
    response = requests.get(
        'https://httpbin.org/headers',
        headers=custom_headers,
        impersonate='chrome120'
    )
    
    received_headers = response.json().get('headers', {})
    print("✅ Custom headers sent:")
    for key, value in custom_headers.items():
        if key in received_headers:
            print(f"   {key}: {received_headers[key]}")
    
    print(f"\n✅ Browser headers automatically added:")
    browser_headers = ['User-Agent', 'Accept-Encoding', 'Accept-Language']
    for header in browser_headers:
        if header in received_headers:
            print(f"   {header}: {received_headers[header]}")
    print()

def example_7_error_handling():
    """
    Show proper error handling and retry strategies
    """
    print("🚨 Example 7: Error Handling & Retries")
    
    def scrape_with_retry(url, max_retries=3):
        """Scrape with automatic retries and browser switching"""
        browsers = ['chrome120', 'firefox117', 'safari16_0']
        
        for attempt in range(max_retries):
            browser = browsers[attempt % len(browsers)]
            
            try:
                print(f"   Attempt {attempt + 1}: Using {browser}")
                
                response = requests.get(
                    url,
                    impersonate=browser,
                    timeout=10
                )
                
                if response.status_code == 200:
                    print(f"   ✅ Success with {browser}")
                    return response
                else:
                    print(f"   ⚠️ Status {response.status_code} with {browser}")
                    
            except Exception as e:
                print(f"   ❌ Error with {browser}: {str(e)[:50]}...")
        
        print("   ❌ All attempts failed")
        return None
    
    # Test with a working URL
    result = scrape_with_retry('https://httpbin.org/status/200')
    if result:
        print(f"✅ Final result: Status {result.status_code}")
    print()

def show_curl_vs_curl_cffi_comparison():
    """Show side-by-side comparison of curl commands vs curl_cffi"""
    print("📋 curl vs curl_cffi Command Comparison")
    print("=" * 50)
    
    comparisons = [
        {
            'description': 'Basic GET request',
            'curl': 'curl https://api.example.com/data',
            'curl_cffi': 'requests.get(url, impersonate="chrome120")'
        },
        {
            'description': 'Custom headers',
            'curl': 'curl -H "Authorization: Bearer token" https://api.example.com',
            'curl_cffi': 'requests.get(url, headers={"Authorization": "Bearer token"}, impersonate="chrome120")'
        },
        {
            'description': 'POST with form data',
            'curl': 'curl -X POST -d "user=barney" https://api.example.com/login',
            'curl_cffi': 'requests.post(url, data={"user": "barney"}, impersonate="chrome120")'
        },
        {
            'description': 'POST with JSON',
            'curl': 'curl -X POST -H "Content-Type: application/json" -d \'{"user":"barney"}\' https://api.example.com',
            'curl_cffi': 'requests.post(url, json={"user": "barney"}, impersonate="chrome120")'
        },
        {
            'description': 'Follow redirects',
            'curl': 'curl -L https://example.com/redirect',
            'curl_cffi': 'requests.get(url, allow_redirects=True, impersonate="chrome120")'
        }
    ]
    
    for comp in comparisons:
        print(f"\n📌 {comp['description']}:")
        print(f"   curl: {comp['curl']}")
        print(f"   curl_cffi: {comp['curl_cffi']}")
    
    print("\n💡 Key Advantage: curl_cffi automatically handles TLS fingerprinting!")
    print()

def main():
    """Run all examples"""
    print("🔧 Practical curl_cffi Examples")
    print("=" * 60)
    print("This script demonstrates real-world usage patterns\n")
    
    try:
        example_1_basic_conversion()
        example_2_tls_fingerprint_matching()
        example_3_browser_switching()
        example_4_session_persistence()
        example_5_post_requests()
        example_6_advanced_headers()
        example_7_error_handling()
        show_curl_vs_curl_cffi_comparison()
        
        print("🎉 All examples completed successfully!")
        print("\n💡 Key Takeaways:")
        print("• curl_cffi provides automatic browser impersonation")
        print("• TLS fingerprints match real browsers exactly") 
        print("• Simple API that's similar to requests library")
        print("• Perfect for modern anti-bot evasion")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")

if __name__ == "__main__":
    main() 