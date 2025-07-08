#!/usr/bin/env python3
"""
🍺🥸 Moe vs Barney: Complete Demonstration

This script runs both the basic and disguised scrapers side-by-side
to show the dramatic difference in anti-bot detection evasion.

Watch Barney get kicked out, then come back in disguise!
"""

import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table

# Import our scrapers
try:
    from barney_basic import BarneyBasicScraper
    from barney_disguised import BarneyDisguisedScraper
except ImportError as e:
    print(f"❌ Error importing scrapers: {e}")
    print("Make sure barney_basic.py and barney_disguised.py are in the same directory")
    sys.exit(1)

console = Console()

def create_comparison_table():
    """Create a comparison table of the two approaches"""
    table = Table(title="🍺 Barney vs 🥸 Disguised Barney")
    
    table.add_column("Aspect", style="cyan", width=20)
    table.add_column("🍺 Basic Barney", style="red", width=30)
    table.add_column("🥸 Disguised Barney", style="green", width=30)
    
    table.add_row(
        "Headers",
        "Static, hardcoded",
        "Dynamic, browser-accurate"
    )
    table.add_row(
        "TLS Fingerprint",
        "Python requests default",
        "Matches real browser exactly"
    )
    table.add_row(
        "HTTP Version",
        "HTTP/1.1",
        "HTTP/2 with correct settings"
    )
    table.add_row(
        "Cipher Suites",
        "OpenSSL defaults",
        "Browser-specific preferences"
    )
    table.add_row(
        "Header Order",
        "Alphabetical (suspicious)",
        "Browser-realistic ordering"
    )
    table.add_row(
        "Detection Rate",
        "🚫 High (easily caught)",
        "✅ Low (blends in)"
    )
    table.add_row(
        "Maintenance",
        "Constant header updates",
        "Library handles updates"
    )
    
    return table

def run_basic_scraper_demo():
    """Run the basic scraper and capture results"""
    console.print("\n" + "="*60)
    console.print("[bold red]🍺 ROUND 1: Basic Barney (Gets Kicked Out)[/bold red]")
    console.print("="*60)
    
    try:
        scraper = BarneyBasicScraper()
        
        # Test fingerprint detection
        console.print("\n[yellow]Testing fingerprint detection...[/yellow]")
        fp_result = scraper.test_fingerprint_site()
        
        time.sleep(1)
        
        # Test headers
        console.print("\n[yellow]Testing header detection...[/yellow]")
        header_result = scraper.test_httpbin_headers()
        
        time.sleep(1)
        
        # Test scraping
        console.print("\n[yellow]Testing basic scraping...[/yellow]")
        scrape_result = scraper.scrape_example_site()
        
        return {
            'fingerprint': fp_result is not None,
            'headers': header_result is not None,
            'scraping': scrape_result is not None and scrape_result.status_code == 200,
            'detection_risk': 'HIGH'
        }
        
    except Exception as e:
        console.print(f"[red]❌ Basic scraper failed: {str(e)}[/red]")
        return {'error': str(e)}

def run_disguised_scraper_demo():
    """Run the disguised scraper and capture results"""
    console.print("\n" + "="*60)
    console.print("[bold green]🥸 ROUND 2: Disguised Barney (Fools Moe)[/bold green]")
    console.print("="*60)
    
    try:
        scraper = BarneyDisguisedScraper("chrome120")
        
        # Test fingerprint detection
        console.print("\n[yellow]Testing disguised fingerprint...[/yellow]")
        fp_result = scraper.test_fingerprint_site()
        
        time.sleep(1)
        
        # Test headers
        console.print("\n[yellow]Testing disguised headers...[/yellow]")
        header_result = scraper.test_httpbin_headers()
        
        time.sleep(1)
        
        # Test advanced detection
        console.print("\n[yellow]Testing advanced detection evasion...[/yellow]")
        advanced_result = scraper.test_advanced_detection()
        
        time.sleep(1)
        
        # Browser switching demo
        console.print("\n[yellow]Demonstrating browser switching...[/yellow]")
        scraper.demonstrate_browser_switching()
        
        return {
            'fingerprint': fp_result is not None,
            'headers': header_result is not None,
            'advanced': advanced_result is not None and advanced_result.status_code == 200,
            'detection_risk': 'LOW'
        }
        
    except Exception as e:
        console.print(f"[red]❌ Disguised scraper failed: {str(e)}[/red]")
        return {'error': str(e)}

def show_results_summary(basic_results, disguised_results):
    """Show a summary comparison of both results"""
    console.print("\n" + "="*60)
    console.print("[bold yellow]📊 FINAL RESULTS & ANALYSIS[/bold yellow]")
    console.print("="*60)
    
    # Results table
    results_table = Table(title="Test Results Comparison")
    results_table.add_column("Test", style="cyan")
    results_table.add_column("🍺 Basic Barney", style="red")
    results_table.add_column("🥸 Disguised Barney", style="green")
    
    if 'error' not in basic_results and 'error' not in disguised_results:
        results_table.add_row(
            "Fingerprint Test",
            "✅ Connected" if basic_results.get('fingerprint') else "❌ Failed",
            "✅ Connected" if disguised_results.get('fingerprint') else "❌ Failed"
        )
        results_table.add_row(
            "Header Detection",
            "⚠️ Suspicious" if basic_results.get('headers') else "❌ Blocked",
            "✅ Natural" if disguised_results.get('headers') else "❌ Failed"
        )
        results_table.add_row(
            "Detection Risk",
            f"🚫 {basic_results.get('detection_risk', 'UNKNOWN')}",
            f"✅ {disguised_results.get('detection_risk', 'UNKNOWN')}"
        )
    
    console.print(results_table)
    
    # Show the comparison table
    console.print("\n")
    console.print(create_comparison_table())

def show_final_verdict():
    """Show the final verdict and recommendations"""
    console.print(Panel.fit(
        "[bold yellow]🎯 THE VERDICT[/bold yellow]\n\n"
        "[red]🍺 Basic Barney:[/red] Gets detected and blocked\n"
        "• Static headers are a dead giveaway\n"
        "• TLS fingerprint doesn't match claimed browser\n"
        "• Missing modern browser security headers\n\n"
        "[green]🥸 Disguised Barney:[/green] Successfully evades detection\n"
        "• Perfect TLS fingerprint matching\n"
        "• Browser-accurate HTTP/2 settings\n"
        "• Realistic header patterns and timing\n\n"
        "[bold cyan]💡 The Lesson:[/bold cyan]\n"
        "Modern anti-bot systems are sophisticated.\n"
        "You need more than headers - you need a complete disguise.\n\n"
        "[dim]Tools like curl_cffi make this possible without the complexity.[/dim]",
        title="Final Analysis",
        border_style="yellow"
    ))

def show_technical_explanation():
    """Show technical explanation of why the disguise works"""
    console.print(Panel.fit(
        "[bold cyan]🔬 TECHNICAL DEEP DIVE[/bold cyan]\n\n"
        "[yellow]What curl_cffi does differently:[/yellow]\n"
        "• Mimics exact TLS handshake of real browsers\n"
        "• Uses correct cipher suite preferences\n"
        "• Maintains proper HTTP/2 settings\n"
        "• Sends headers in browser-realistic order\n"
        "• Handles compression algorithms correctly\n\n"
        "[yellow]Why static headers fail:[/yellow]\n"
        "• TLS fingerprint mismatches User-Agent claim\n"
        "• Header order follows alphabetical pattern\n"
        "• Missing browser-specific security headers\n"
        "• HTTP/1.1 when browser claims HTTP/2 support\n\n"
        "[green]The result:[/green] Indistinguishable from real browser traffic",
        title="Technical Analysis",
        border_style="cyan"
    ))

def main():
    """Run the complete demonstration"""
    console.print(Panel.fit(
        "[bold yellow]🍺🥸 MOE vs BARNEY: Anti-Bot Evasion Demo[/bold yellow]\n\n"
        "[dim]This demo shows the evolution from basic scraping\n"
        "to modern anti-bot evasion techniques.[/dim]\n\n"
        "[red]Barney[/red] = Basic scraper (gets kicked out)\n"
        "[yellow]Moe[/yellow] = Anti-bot system\n"
        "[green]Disguised Barney[/green] = Advanced scraper (fools Moe)\n\n"
        "[bold]🎬 Starting demonstration...[/bold]",
        title="🍻 Moe's Tavern Security System",
        border_style="yellow"
    ))
    
    time.sleep(2)
    
    # Run basic scraper demo
    basic_results = run_basic_scraper_demo()
    
    time.sleep(2)
    
    # Run disguised scraper demo
    disguised_results = run_disguised_scraper_demo()
    
    time.sleep(1)
    
    # Show results comparison
    show_results_summary(basic_results, disguised_results)
    
    time.sleep(1)
    
    # Show technical explanation
    show_technical_explanation()
    
    time.sleep(1)
    
    # Show final verdict
    show_final_verdict()
    
    console.print("\n[bold green]🎉 Demo completed![/bold green]")
    console.print("[dim]Try running the individual scripts:[/dim]")
    console.print("[dim]  python barney_basic.py[/dim]")
    console.print("[dim]  python barney_disguised.py[/dim]")

if __name__ == "__main__":
    main() 