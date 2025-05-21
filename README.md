# OpenHands Documentation (Mintlify)

This repository contains the Mintlify documentation for the [OpenHands](https://github.com/All-Hands-AI/OpenHands) project.

## Migration from Docusaurus

The documentation was migrated from Docusaurus to Mintlify using the following process:

1. Created a basic Mintlify structure with `docs.json` configuration
2. Developed a Python script (`convert_docs.py`) to convert Docusaurus markdown files to Mintlify format
3. Organized content following Mintlify's recommended structure
4. Fixed image paths and internal links
5. Created a proper navigation structure in `docs.json`
6. Customized the theme with OpenHands branding colors

## Structure

- `/api-reference`: API documentation
- `/essentials`: Mintlify essentials documentation
- `/images`: All documentation images
- `/snippets`: Reusable code snippets
- `/usage`: Main OpenHands documentation

## Local Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of your documentation (where mint.json is)

```
mintlify dev
```

The documentation will be available at http://localhost:3000.

## Deployment

To deploy the documentation to Mintlify:

1. Push the changes to the repository
2. Connect the repository to Mintlify
3. Configure the deployment settings in Mintlify

## Known Issues

There are some parsing errors in the MDX files that need to be fixed:
- Some files contain invalid image syntax
- Some files have Docusaurus-specific components that need to be replaced

## Resources

- [Mintlify Documentation](https://mintlify.com/docs)
- [Docusaurus to Mintlify Migration Guide](https://ritza.co/articles/docusaurus-to-mintlify-migration/)

## Troubleshooting

- Mintlify dev isn't running - Run `mintlify install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `mint.json`
