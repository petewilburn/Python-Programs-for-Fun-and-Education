# Mermaid Dark Mode Configuration Guide

## Overview
This document explains the dark mode fixes applied to Mermaid charts in the repository and provides alternative theme configurations for different platforms and preferences.

## What Was Fixed
All Mermaid charts in the markdown files have been updated with dark mode friendly themes to ensure readability in both light and dark mode environments including:
- VS Code Dark Theme
- GitHub Dark Theme  
- GitLab Dark Theme
- Other markdown viewers with dark themes

## Current Dark Theme Configuration
The default dark theme applied to all charts uses:

```javascript
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#4f46e5','primaryTextColor':'#ffffff','primaryBorderColor':'#6366f1','lineColor':'#6b7280','secondaryColor':'#10b981','tertiaryColor':'#f59e0b','background':'#1f2937','mainBkg':'#374151','secondBkg':'#4b5563','tertiaryBkg':'#6b7280'}}}%%
```

### Color Scheme Breakdown:
- **Primary Color**: `#4f46e5` (Indigo) - Main nodes and elements
- **Primary Text**: `#ffffff` (White) - Text on primary elements  
- **Primary Border**: `#6366f1` (Light Indigo) - Borders and outlines
- **Line Color**: `#6b7280` (Gray) - Connecting lines and arrows
- **Secondary**: `#10b981` (Emerald) - Secondary elements
- **Tertiary**: `#f59e0b` (Amber) - Tertiary elements
- **Background**: `#1f2937` (Dark Gray) - Chart background
- **Main Background**: `#374151` (Medium Gray) - Node backgrounds
- **Secondary Background**: `#4b5563` (Light Gray) - Alternative backgrounds

## Alternative Theme Options

### 1. High Contrast Dark Theme
For maximum readability in dark environments:

```mermaid

```

### 2. Blue Professional Theme
Corporate-friendly dark theme:

```mermaid

```

### 3. GitHub Compatible Theme
Optimized for GitHub's dark theme:

```mermaid

```

### 4. Neutral Adaptive Theme
Works well in both light and dark modes:

```mermaid

```

## Files Updated

The following files were automatically updated with dark mode themes:

1. **IBKR_Trading_System_Architecture.md** - 7 charts updated
2. **Hierarchical_Swarm_Enterprise_Architecture.md** - 12 charts updated  
3. **IBKR_API_Comparison_Guide.md** - 8 charts updated

## Testing Dark Mode

### In VS Code:
1. Switch to dark theme: `Ctrl+K Ctrl+T` → Select dark theme
2. Open any markdown file with Mermaid charts
3. Use Mermaid preview extension to view charts

### On GitHub:
1. Go to Settings → Appearance → Theme → Dark
2. View any markdown file in the repository
3. Mermaid charts should render with appropriate colors

### In Other Platforms:
- **GitLab**: Dark theme support varies by version
- **Notion**: May need manual theme selection
- **Obsidian**: Usually respects system theme

## Manual Theme Customization

To customize a specific chart, add the theme configuration at the top of the Mermaid code block:

```markdown
\`\`\`mermaid
%%{init: {'theme':'[THEME_NAME]', 'themeVariables': {[CUSTOM_VARIABLES]}}}%%
[YOUR_CHART_CODE]
\`\`\`
```

### Available Built-in Themes:
- `default` - Light theme
- `dark` - Dark theme  
- `forest` - Green theme
- `neutral` - Grayscale theme
- `base` - Minimal theme (customizable)

## Troubleshooting

### If Charts Don't Display Properly:

1. **Clear browser cache** - Cached versions may show old theme
2. **Check Mermaid version** - Ensure platform supports theme variables
3. **Validate syntax** - Use [Mermaid Live Editor](https://mermaid.live/) to test
4. **Platform limitations** - Some platforms may not support all theme features

### Common Issues:

- **Text not visible**: Adjust `primaryTextColor` and background colors
- **Lines too faint**: Increase contrast for `lineColor`
- **Poor contrast**: Test themes in both light and dark environments

## Script Usage

The `fix_mermaid_dark_mode.py` script can be run again to:
- Update additional markdown files
- Apply different theme configurations
- Batch process multiple repositories

### Running the Script:
```bash
python src/Python_Programs/fix_mermaid_dark_mode.py
```

## Best Practices

1. **Test in multiple environments** - VS Code, GitHub, etc.
2. **Use semantic colors** - Different colors for different types of nodes
3. **Maintain consistency** - Use same theme across related diagrams
4. **Consider accessibility** - Ensure sufficient color contrast
5. **Document theme choices** - Note why specific themes were chosen

## Future Updates

To update themes in the future:
1. Modify the `DARK_THEME_CONFIG` in the script
2. Re-run the script to apply changes
3. Test across platforms
4. Commit changes to repository

This ensures all Mermaid charts remain readable and professional-looking across all viewing environments.
