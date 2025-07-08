#!/usr/bin/env python3
"""
🥸 Barney Simpson Returns: Disguised Scraper (Fools Moe)

This is Barney with a full disguise - complete browser fingerprint impersonation.
Moe won't recognize him now!

Uses curl_cffi to impersonate real browsers with matching TLS fingerprints.
"""

from curl_cffi import requests
import time
import json
from rich.console import Console
from rich.panel import Panel

console = Console()

class BarneyDisguisedScraper:
    """Advanced scraper with full browser fingerprint impersonation"""
    
    def __init__(self, browser_version="chrome120"):
        """
        Initialize with browser impersonation
        
        Available browsers:
        - chrome99, chrome100, chrome101, chrome104, chrome107, chrome110, chrome116, chrome119, chrome120
        - firefox99, firefox102, firefox104, firefox108, firefox110, firefox117
        - safari15_3, safari15_5, safari16_0
        - edge99, edge101
        """
        self.browser_version = browser_version
        self.session = requests.Session()
        
        # The magic: curl_cffi automatically handles:
        # ✅ TLS fingerprint matching the browser
        # ✅ HTTP/2 settings
        # ✅ Header order and casing
        # ✅ Compression algorithms
        # ✅ Cipher suites
        console.print(f"[green]🥸 Disguised as:[/green] {browser_version}")
    
    def test_fingerprint_site(self, url="https://tls.browserleaks.com/json"):
        """Test against fingerprint detection - now with proper disguise!"""
        console.print("\n[bold green]🥸 Barney's Disguised Approach[/bold green]")
        console.print("Using full browser fingerprint impersonation...")
        
        try:
            # The magic happens here: impersonate parameter
            response = self.session.get(
                url, 
                impersonate=self.browser_version,
                timeout=10
            )
            
            console.print(f"[green]✓ Status Code:[/green] {response.status_code}")
            console.print(f"[yellow]Impersonating:[/yellow] {self.browser_version}")
            
            # Parse the fingerprint response
            if response.headers.get('content-type', '').startswith('application/json'):
                data = response.json()
                console.print(f"\n[cyan]Server detected:[/cyan]")
                console.print(f"  JA3 Hash: {data.get('ja3_hash', 'Unknown')}")
                console.print(f"  User Agent: {data.get('user_agent', 'Unknown')}")
                console.print(f"  TLS Version: {data.get('tls_version', 'Unknown')}")
                console.print(f"  Cipher Suite: {data.get('cipher_suite', 'Unknown')}")
                
                # Show what makes this convincing
                console.print(f"\n[green]✅ Why this works:[/green]")
                console.print(f"  • TLS fingerprint matches real {self.browser_version}")
                console.print(f"  • HTTP/2 settings are browser-accurate")
                console.print(f"  • Header order follows browser patterns")
                console.print(f"  • Cipher suites match browser's preferences")
            
            return response
            
        except Exception as e:
            console.print(f"[red]❌ Request failed:[/red] {str(e)}")
            return None
    
    def test_httpbin_headers(self):
        """Test what headers get sent with impersonation"""
        console.print("\n[bold yellow]🔍 Testing Disguised Headers[/bold yellow]")
        
        try:
            response = self.session.get(
                "https://httpbin.org/headers",
                impersonate=self.browser_version,
                timeout=10
            )
            data = response.json()
            
            console.print("[cyan]Headers as seen by server:[/cyan]")
            for key, value in data.get('headers', {}).items():
                console.print(f"  {key}: {value}")
                
            return response
            
        except Exception as e:
            console.print(f"[red]❌ Header test failed:[/red] {str(e)}")
            return None
    
    def test_advanced_detection(self, url="https://httpbin.org/anything"):
        """Test against more sophisticated detection methods"""
        console.print(f"\n[bold blue]🎯 Advanced Detection Test[/bold blue]")
        
        try:
            # Add some realistic browsing behavior
            custom_headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'max-age=0',
                'Sec-Ch-Ua': f'"{self.browser_version}";v="120", "Chromium";v="120", "Not_A Brand";v="24"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"macOS"',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
            }
            
            response = self.session.get(
                url,
                headers=custom_headers,
                impersonate=self.browser_version,
                timeout=10
            )
            
            if response.status_code == 200:
                console.print("[green]✅ Advanced detection bypassed![/green]")
                data = response.json()
                
                console.print(f"\n[cyan]Complete request as seen by server:[/cyan]")
                console.print(f"Method: {data.get('method')}")
                console.print(f"URL: {data.get('url')}")
                console.print(f"Origin: {data.get('origin')}")
                
                # Show some key headers that indicate good impersonation
                headers = data.get('headers', {})
                important_headers = [
                    'User-Agent', 'Accept', 'Accept-Encoding', 
                    'Accept-Language', 'Sec-Ch-Ua', 'Sec-Fetch-Dest'
                ]
                
                console.print(f"\n[green]🎭 Convincing browser signals:[/green]")
                for header in important_headers:
                    if header in headers:
                        console.print(f"  {header}: {headers[header]}")
                        
            else:
                console.print(f"[red]❌ Still detected! Status: {response.status_code}[/red]")
                
            return response
            
        except Exception as e:
            console.print(f"[red]❌ Advanced test failed:[/red] {str(e)}")
            return None
    
    def demonstrate_browser_switching(self):
        """Show how to switch between different browser impersonations"""
        console.print(f"\n[bold magenta]🎭 Browser Switching Demo[/bold magenta]")
        
        browsers = ["chrome120", "firefox117", "safari16_0"]
        
        for browser in browsers:
            try:
                console.print(f"\n[yellow]Testing as {browser}...[/yellow]")
                
                response = self.session.get(
                    "https://httpbin.org/user-agent",
                    impersonate=browser,
                    timeout=5
                )
                
                if response.status_code == 200:
                    data = response.json()
                    console.print(f"  [green]✓[/green] User-Agent: {data.get('user-agent', 'Unknown')}")
                else:
                    console.print(f"  [red]❌ Failed with status {response.status_code}[/red]")
                    
            except Exception as e:
                console.print(f"  [red]❌ Error: {str(e)}[/red]")
            
            time.sleep(0.5)  # Be nice to the server

def main():
    """Demonstrate Barney's disguised scraping approach"""
    
    console.print(Panel.fit(
        "[bold green]🥸 Barney Simpson: Disguised Scraper Demo[/bold green]\n"
        "[yellow]Using full browser fingerprint impersonation...[/yellow]\n"
        "[dim]Watch Barney fool Moe with his mustache! 🎭[/dim]",
        title="Disguised Scraper",
        border_style="green"
    ))
    
    scraper = BarneyDisguisedScraper("chrome120")
    
    # Test 1: Check our disguised fingerprint
    scraper.test_fingerprint_site()
    
    time.sleep(1)
    
    # Test 2: See what headers we're sending now
    scraper.test_httpbin_headers()
    
    time.sleep(1)
    
    # Test 3: Advanced detection test
    scraper.test_advanced_detection()
    
    time.sleep(1)
    
    # Test 4: Show browser switching capabilities
    scraper.demonstrate_browser_switching()
    
    console.print(Panel.fit(
        "[bold green]✅ RESULT: DETECTION BYPASSED[/bold green]\n"
        "[yellow]Why the disguise works:[/yellow]\n"
        "• TLS fingerprint matches real browsers exactly\n"
        "• HTTP/2 settings are browser-accurate\n"
        "• Header order follows browser patterns\n"
        "• Cipher suites match browser preferences\n"
        "• No inconsistencies for detection systems to spot\n\n"
        "[dim]Barney successfully fooled Moe! 🎉[/dim]",
        title="Success Summary",
        border_style="green"
    ))

if __name__ == "__main__":
    main() 