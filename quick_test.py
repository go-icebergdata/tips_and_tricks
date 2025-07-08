#!/usr/bin/env python3
"""
🧪 Quick Test: Verify curl_cffi Installation

Simple test to make sure everything is working before running the full demo.
"""

def test_imports():
    """Test if all required packages can be imported"""
    print("🔍 Testing imports...")
    
    try:
        from curl_cffi import requests
        print("✅ curl_cffi imported successfully")
    except ImportError as e:
        print(f"❌ curl_cffi import failed: {e}")
        return False
    
    try:
        from rich.console import Console
        print("✅ rich imported successfully")
    except ImportError as e:
        print(f"❌ rich import failed: {e}")
        return False
    
    try:
        from fake_useragent import UserAgent
        print("✅ fake_useragent imported successfully")
    except ImportError as e:
        print(f"❌ fake_useragent import failed: {e}")
        return False
    
    return True

def test_basic_request():
    """Test a basic curl_cffi request"""
    print("\n🌐 Testing basic curl_cffi request...")
    
    try:
        from curl_cffi import requests
        
        response = requests.get(
            'https://httpbin.org/user-agent',
            impersonate='chrome120',
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            user_agent = data.get('user-agent', 'Unknown')
            print(f"✅ Request successful!")
            print(f"   User-Agent detected: {user_agent[:50]}...")
            return True
        else:
            print(f"❌ Request failed with status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return False

def test_fingerprint():
    """Test TLS fingerprint detection"""
    print("\n🔒 Testing TLS fingerprint...")
    
    try:
        from curl_cffi import requests
        
        response = requests.get(
            'https://tls.browserleaks.com/json',
            impersonate='chrome120',
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            ja3 = data.get('ja3_hash', 'Unknown')
            print(f"✅ TLS fingerprint test successful!")
            print(f"   JA3 Hash: {ja3}")
            return True
        else:
            print(f"❌ Fingerprint test failed with status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Fingerprint test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Quick Test Suite for Moe vs Barney Demo")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed. Please install requirements:")
        print("   pip install -r requirements.txt")
        return False
    
    # Test basic functionality
    if not test_basic_request():
        print("\n❌ Basic request test failed.")
        return False
    
    # Test fingerprint detection
    if not test_fingerprint():
        print("\n❌ Fingerprint test failed.")
        return False
    
    print("\n🎉 All tests passed!")
    print("\n✅ Ready to run the full demo:")
    print("   python demo.py              # Full side-by-side comparison")
    print("   python barney_basic.py      # Basic scraper only")
    print("   python barney_disguised.py  # Disguised scraper only")
    print("   python examples.py          # Practical examples")
    
    return True

if __name__ == "__main__":
    main() 