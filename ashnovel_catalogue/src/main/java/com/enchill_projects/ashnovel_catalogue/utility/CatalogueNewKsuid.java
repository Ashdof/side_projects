/**
 * ID generator
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.utility;

import com.github.ksuid.Ksuid;

public class CatalogueNewKsuid {

    /**
     * New ID:
     * generate a new Ksuid-based id
     * @return the generated string
     */
    public static String generateNewKsuid() {
        Ksuid ksuid = Ksuid.newKsuid();

        return ksuid.toString();
    }
}
