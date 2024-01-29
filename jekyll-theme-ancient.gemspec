# frozen_string_literal: true

Gem::Specification.new do |s|
  s.name          = "jekyll-theme-ancient"
  s.version       = "0.0.0"
  s.license       = "Apache-2.0"
  s.authors       = ["Mark Kettner"]
  s.email         = ["none"]
  s.homepage      = "https://github.com/mkettn/ancient-theme"
  s.summary       = "Ancient is a Jekyll theme for GitHub Pages"

  s.files         = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r{^((_includes|_layouts|_sass|assets)/|(LICENSE|README)((\.(txt|md|markdown)|$)))}i)
  end

  s.required_ruby_version = ">= 2.4.0"

  s.platform = Gem::Platform::RUBY
  s.add_runtime_dependency "jekyll", "> 3.5", "< 5.0"
end
